"""aaaa

Revision ID: eee738780acb
Revises: f11f09ac3cb6
Create Date: 2020-07-30 00:38:49.808258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eee738780acb'
down_revision = 'f11f09ac3cb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sewa_locker', sa.Column('akses', sa.String(length=8), nullable=True))
    op.drop_column('users', 'packet2')
    op.drop_column('users', 'packet4')
    op.drop_column('users', 'packet5')
    op.drop_column('users', 'packet3')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('packet3', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('packet5', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('packet4', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('packet2', sa.VARCHAR(), nullable=True))
    op.drop_column('sewa_locker', 'akses')
    # ### end Alembic commands ###