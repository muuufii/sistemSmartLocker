"""update baru

Revision ID: 28745f343095
Revises: 2579054181e1
Create Date: 2020-05-07 10:45:42.359619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28745f343095'
down_revision = '2579054181e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locker_command', sa.Column('verifpin', sa.Integer(), nullable=True))
    op.add_column('sewa_locker', sa.Column('userpin', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sewa_locker', 'userpin')
    op.drop_column('locker_command', 'verifpin')
    # ### end Alembic commands ###
