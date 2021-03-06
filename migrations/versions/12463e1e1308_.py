"""empty message

Revision ID: 12463e1e1308
Revises: b12a7d8aefd5
Create Date: 2019-09-30 17:30:30.611551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12463e1e1308'
down_revision = 'b12a7d8aefd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_constraint('flask_dance_oauth_user_id_fkey', 'flask_dance_oauth', type_='foreignkey')
    op.create_foreign_key(None, 'flask_dance_oauth', 'users', ['user_id'], ['id'])
    op.drop_constraint('profile_user_id_fkey', 'profile', type_='foreignkey')
    op.create_foreign_key(None, 'profile', 'users', ['user_id'], ['id'])
    op.drop_constraint('token_user_id_fkey', 'token', type_='foreignkey')
    op.create_foreign_key(None, 'token', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'token', type_='foreignkey')
    op.create_foreign_key('token_user_id_fkey', 'token', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'profile', type_='foreignkey')
    op.create_foreign_key('profile_user_id_fkey', 'profile', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'flask_dance_oauth', type_='foreignkey')
    op.create_foreign_key('flask_dance_oauth_user_id_fkey', 'flask_dance_oauth', 'user', ['user_id'], ['id'])
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_period', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    # ### end Alembic commands ###
