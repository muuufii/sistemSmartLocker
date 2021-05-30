"""wwra

Revision ID: 0da106aaea49
Revises: 1242e96a4bbb
Create Date: 2020-08-31 19:09:37.657314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0da106aaea49'
down_revision = '1242e96a4bbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locker_command', sa.Column('enroll_fingerprint', sa.String(length=8), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locker_command', 'enroll_fingerprint')
    # ### end Alembic commands ###
