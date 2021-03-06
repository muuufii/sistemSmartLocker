"""aa

Revision ID: 421a38f2c9ca
Revises: 28745f343095
Create Date: 2020-06-23 11:03:13.551997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '421a38f2c9ca'
down_revision = '28745f343095'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sewa_locker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('sewa', sa.Integer(), nullable=True),
    sa.Column('nomorlocker', sa.String(length=32), nullable=True),
    sa.Column('finger_data', sa.String(length=128), nullable=True),
    sa.Column('userpin', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sewa_loker')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sewa_loker',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('sewa', sa.INTEGER(), nullable=True),
    sa.Column('nomorlocker', sa.VARCHAR(length=32), nullable=True),
    sa.Column('finger_data', sa.VARCHAR(length=128), nullable=True),
    sa.Column('userpin', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sewa_locker')
    # ### end Alembic commands ###
