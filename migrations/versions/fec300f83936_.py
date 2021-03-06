"""empty message

Revision ID: fec300f83936
Revises: 2de68abae262
Create Date: 2019-09-27 23:01:30.832578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fec300f83936'
down_revision = '2de68abae262'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('baby',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('baby')
    # ### end Alembic commands ###
