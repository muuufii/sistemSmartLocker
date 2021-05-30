"""wwra

Revision ID: 582807e8c2c4
Revises: 0da106aaea49
Create Date: 2020-08-31 19:31:01.818893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '582807e8c2c4'
down_revision = '0da106aaea49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locker_command', sa.Column('enroll', sa.String(length=8), nullable=True))
    op.drop_column('locker_command', 'enroll_fingerprint')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locker_command', sa.Column('enroll_fingerprint', sa.VARCHAR(length=8), nullable=True))
    op.drop_column('locker_command', 'enroll')
    # ### end Alembic commands ###