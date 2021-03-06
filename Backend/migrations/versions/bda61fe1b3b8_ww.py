"""ww

Revision ID: bda61fe1b3b8
Revises: 272f4d2611d5
Create Date: 2020-08-14 13:10:38.514506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bda61fe1b3b8'
down_revision = '272f4d2611d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locker_command', sa.Column('enroll_locker', sa.String(length=8), nullable=True))
    op.add_column('locker_command', sa.Column('uid_locker1', sa.Integer(), nullable=True))
    op.add_column('locker_command', sa.Column('uid_locker2', sa.Integer(), nullable=True))
    op.add_column('locker_command', sa.Column('unlock_locker1', sa.String(length=8), nullable=True))
    op.add_column('locker_command', sa.Column('unlock_locker2', sa.String(length=8), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locker_command', 'unlock_locker2')
    op.drop_column('locker_command', 'unlock_locker1')
    op.drop_column('locker_command', 'uid_locker2')
    op.drop_column('locker_command', 'uid_locker1')
    op.drop_column('locker_command', 'enroll_locker')
    # ### end Alembic commands ###
