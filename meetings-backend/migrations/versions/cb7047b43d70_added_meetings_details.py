"""Added meetings.details

Revision ID: cb7047b43d70
Revises: 9839dd0994b9
Create Date: 2022-01-03 04:55:06.444917

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "cb7047b43d70"
down_revision = "9839dd0994b9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("meetings", sa.Column("details", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("meetings", "details")
    # ### end Alembic commands ###