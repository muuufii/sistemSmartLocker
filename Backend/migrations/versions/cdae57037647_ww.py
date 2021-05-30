"""ww

Revision ID: cdae57037647
Revises: b50604feba82
Create Date: 2020-08-19 11:53:52.843071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdae57037647'
down_revision = 'b50604feba82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locker_command', sa.Column('hasil', sa.String(length=8), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locker_command', 'hasil')
    # ### end Alembic commands ###