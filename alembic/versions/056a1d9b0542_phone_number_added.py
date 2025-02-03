"""phone number added

Revision ID: 056a1d9b0542
Revises: 
Create Date: 2025-01-27 15:32:23.950491

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '056a1d9b0542'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    #op.add_column('users',sa.Column('phone number', sa.String(), nullable=True))
    pass

def downgrade() -> None:
    op.drop_column("users", "phone number")
