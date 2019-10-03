"""empty message

Revision ID: ae9ba26ac63d
Revises: 56095ff04924
Create Date: 2019-10-02 17:07:04.026352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae9ba26ac63d'
down_revision = '56095ff04924'
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
    op.create_table('nutrition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.Column('reviewby', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nutrition')
    op.drop_table('baby')
    # ### end Alembic commands ###
