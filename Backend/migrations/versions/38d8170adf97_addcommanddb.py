"""addcommanddb

Revision ID: 38d8170adf97
Revises: 2439d3cd762e
Create Date: 2020-04-10 19:46:04.529893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38d8170adf97'
down_revision = '2439d3cd762e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locker_command',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fingerprintenroll', sa.String(length=32), nullable=True),
    sa.Column('lockercontrol', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('locker_command')
    # ### end Alembic commands ###
