import os
from .. import mail
from flask import render_template, url_for, flash, redirect, request, Blueprint, url_for, current_app
from flask_login import login_user, current_user, logout_user, login_required
from app import db  
from app.models import User, Post, Comment
from app.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm)
import secrets
# from PIL import Image
from flask_mail import Message
# from ..email import mail_message
from app.requests import get_quote
from .import users

# from app import mail

# users = Blueprint('users', __name__)
# quotes = get_quote()


@users.route("/register", methods=['GET', 'POST'])
def register():
     

    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
                
        flash('Your account has been created! You are now able to log in', 'success')
        # mail_message("Welcome to FLASK BLOG","email/welcome_user",user.email,user=user)

        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid Username or Password')
    
    title = "login"
    return render_template('login.html',form = form,title=title)


   
   
    # if current_user.is_authenticated:
    #     return redirect(url_for('main.home'))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user, remember=form.remember.data)
    #         next_page = request.args.get('next')
    #         return redirect(next_page) if next_page else redirect(url_for('main.home'))
    #     else:
    #         flash('Login Unsuccessful. Please check email and password', 'danger')
    # return render_template('login.html', title='Login', form=form, quotes=quotes)
    
    


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))


def save_picture(form_picture):
    randome_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_name = randome_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_name)
    
    output_size = (125, 125)
    final_image = Image.open(form_picture)
    final_image.thumbnail(output_size)
    
    final_image.save(picture_path)
    image_files = url_for('static', filename='profile_pics/' + current_user.image)
    return picture_name
    
    
@users.route("/account",  methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image = picture_file
            
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        
        flash('Your account has been updated.', 'success')
        return redirect(url_for('users.account'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        
    
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=current_user.username).first_or_404()
    myposts = Post.query.order_by(Post.posted_date.desc())
    return render_template('account.html', title='Account', user=user, form=form, myposts=myposts)


@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.posted_date.desc()).paginate(page=page, per_page=7)
    myposts = Post.query.order_by(Post.posted_date.desc())
    return render_template('userposts.html', posts=posts, user=user, myposts=myposts)