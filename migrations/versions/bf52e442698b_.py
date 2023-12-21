"""empty message

Revision ID: bf52e442698b
Revises: 21ab299d9e0f
Create Date: 2023-12-21 09:06:10.822466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf52e442698b'
down_revision = '21ab299d9e0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('address')
        batch_op.drop_column('key')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('key', sa.VARCHAR(length=80), nullable=False))
        batch_op.add_column(sa.Column('address', sa.VARCHAR(length=80), nullable=False))

    # ### end Alembic commands ###
