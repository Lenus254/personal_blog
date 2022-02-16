"""fourth migration

Revision ID: b07eaf610560
Revises: fa5b56a5df2c
Create Date: 2022-02-15 21:35:03.428240

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b07eaf610560'
down_revision = 'fa5b56a5df2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('post', 'posted_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('post', 'content',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('post', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('post', 'content',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('post', 'posted_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('post', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###