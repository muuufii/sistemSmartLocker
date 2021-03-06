"""www

Revision ID: 1c914f9e0517
Revises: 0701d25e883f
Create Date: 2020-08-16 16:08:41.014033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c914f9e0517'
down_revision = '0701d25e883f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locker_command', sa.Column('enroll_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locker_command', 'enroll_id')
    # ### end Alembic commands ###
