"""wwaaa

Revision ID: 14d46044c4f2
Revises: fd7536fe18c2
Create Date: 2020-07-30 00:36:31.275268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14d46044c4f2'
down_revision = 'fd7536fe18c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locker_command', 'lockercontrol')
    op.drop_column('locker_command', 'fingerprintenroll')
    op.drop_column('locker_command', 'verifpin')
    op.add_column('sewa_locker', sa.Column('akses', sa.String(length=8), nullable=True))
    op.drop_column('sewa_locker', 'packet4')
    op.drop_column('sewa_locker', 'packet5')
    op.drop_column('sewa_locker', 'packet2')
    op.drop_column('sewa_locker', 'packet3')
    op.drop_column('users', 'packet4')
    op.drop_column('users', 'packet5')
    op.drop_column('users', 'packet2')
    op.drop_column('users', 'packet3')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('packet3', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('packet2', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('packet5', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('packet4', sa.VARCHAR(), nullable=True))
    op.add_column('sewa_locker', sa.Column('packet3', sa.VARCHAR(), nullable=True))
    op.add_column('sewa_locker', sa.Column('packet2', sa.VARCHAR(), nullable=True))
    op.add_column('sewa_locker', sa.Column('packet5', sa.VARCHAR(), nullable=True))
    op.add_column('sewa_locker', sa.Column('packet4', sa.VARCHAR(), nullable=True))
    op.drop_column('sewa_locker', 'akses')
    op.add_column('locker_command', sa.Column('verifpin', sa.INTEGER(), nullable=True))
    op.add_column('locker_command', sa.Column('fingerprintenroll', sa.VARCHAR(length=32), nullable=True))
    op.add_column('locker_command', sa.Column('lockercontrol', sa.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###