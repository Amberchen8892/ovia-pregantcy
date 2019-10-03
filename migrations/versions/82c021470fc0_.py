"""empty message

Revision ID: 82c021470fc0
Revises: 1aaeccf74a0f
Create Date: 2019-09-30 13:43:43.523799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82c021470fc0'
down_revision = '1aaeccf74a0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('last_period', sa.String(), nullable=True),
    sa.Column('date_conception', sa.String(), nullable=True),
    sa.Column('due_date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('last_period', sa.String(), nullable=True))
    op.drop_column('user', 'duedate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('duedate', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('user', 'last_period')
    op.drop_table('profile')
    # ### end Alembic commands ###
