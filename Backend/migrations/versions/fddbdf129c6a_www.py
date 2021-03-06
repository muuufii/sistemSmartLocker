"""www

Revision ID: fddbdf129c6a
Revises: f21c6572fbb5
Create Date: 2020-07-29 21:57:16.664573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fddbdf129c6a'
down_revision = 'f21c6572fbb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sewa_locker', sa.Column('akses', sa.String(length=8), nullable=True))
    op.drop_column('sewa_locker', 'packet2')
    op.drop_column('sewa_locker', 'packet3')
    op.drop_column('sewa_locker', 'packet5')
    op.drop_column('sewa_locker', 'packet4')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sewa_locker', sa.Column('packet4', sa.VARCHAR(), nullable=True))
    op.add_column('sewa_locker', sa.Column('packet5', sa.VARCHAR(), nullable=True))
    op.add_column('sewa_locker', sa.Column('packet3', sa.VARCHAR(), nullable=True))
    op.add_column('sewa_locker', sa.Column('packet2', sa.VARCHAR(), nullable=True))
    op.drop_column('sewa_locker', 'akses')
    # ### end Alembic commands ###
