from flask import render_template, request, Blueprint
from app.models import Post
from app.requests import get_quote
from .import main



@main.route("/")
def index():
    quotes = get_quote()  
    
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.posted_date.desc()).paginate(page=page, per_page=7)
    myposts = Post.query.order_by(Post.posted_date.desc())
    return render_template('index.html', posts=posts, myposts=myposts ,quotes=quotes)


@main.route("/about")
def about():
    myposts = Post.query.order_by(Post.posted_date.desc())
    return render_template('about.html', title='About', myposts=myposts)


@main.route("/subscribe")
def subscribe():
    return render_template('subscribe.html', title='Subscription')
