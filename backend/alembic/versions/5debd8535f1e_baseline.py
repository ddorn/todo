"""baseline

Revision ID: 5debd8535f1e
Revises:
Create Date: 2021-02-27 21:53:01.744010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5debd8535f1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('todos', sa.Column('important', sa.Boolean(), server_default="0"))


def downgrade():
    op.drop_column('todos', 'important')
