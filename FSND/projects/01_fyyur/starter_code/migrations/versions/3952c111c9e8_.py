"""empty message

Revision ID: 3952c111c9e8
Revises: a42d57950a9f
Create Date: 2020-10-11 16:34:10.384287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3952c111c9e8'
down_revision = 'a42d57950a9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Show_id_seq"\'::regclass)'), autoincrement=True, nullable=False))
    # ### end Alembic commands ###
