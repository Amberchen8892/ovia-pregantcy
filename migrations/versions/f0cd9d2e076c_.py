"""empty message

Revision ID: f0cd9d2e076c
Revises: e3380d0ea195
Create Date: 2019-09-26 11:45:41.631174

"""
from alembic import op
import sqlalchemy as sa,sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'f0cd9d2e076c'
down_revision = 'e3380d0ea195'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('excercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.Column('reviewby', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('laboranddelivery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lifestyles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('losses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nutrition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.Column('reviewby', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plainning',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pregnancybyweeks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('intro', sa.String(), nullable=False),
    sa.Column('mickey', sa.String(), nullable=False),
    sa.Column('mom', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.Column('reviewby', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('symtoms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.Column('reviewby', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('duedate', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('flask_dance_oauth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('token', sqlalchemy_utils.types.json.JSONType(), nullable=False),
    sa.Column('provider_user_id', sa.String(length=256), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_user_id')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token')
    op.drop_table('flask_dance_oauth')
    op.drop_table('user')
    op.drop_table('symtoms')
    op.drop_table('pregnancybyweeks')
    op.drop_table('plainning')
    op.drop_table('nutrition')
    op.drop_table('losses')
    op.drop_table('lifestyles')
    op.drop_table('laboranddelivery')
    op.drop_table('excercises')
    # ### end Alembic commands ###
