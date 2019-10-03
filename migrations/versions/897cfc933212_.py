"""empty message

Revision ID: 897cfc933212
Revises: 885283b1816e
Create Date: 2019-09-30 16:42:59.595234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '897cfc933212'
down_revision = '885283b1816e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profile', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('profile', sa.Column('last_name', sa.String(), nullable=True))
    op.drop_column('profile', 'last_period')
    op.drop_column('profile', 'email')
    op.drop_column('profile', 'username')
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.add_column('profile', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('profile', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('profile', sa.Column('last_period', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('profile', 'last_name')
    op.drop_column('profile', 'first_name')
    # ### end Alembic commands ###