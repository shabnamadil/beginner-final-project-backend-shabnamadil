"""empty message

Revision ID: e548a257b385
Revises: 6e433872f19b
Create Date: 2023-03-03 14:21:02.571893

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e548a257b385'
down_revision = '6e433872f19b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_index('user_id_product_name')
        batch_op.create_unique_constraint(None, ['product_name'])
        batch_op.drop_column('product_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_index('user_id_product_name', ['user_id', 'product_name'], unique=False)

    # ### end Alembic commands ###
