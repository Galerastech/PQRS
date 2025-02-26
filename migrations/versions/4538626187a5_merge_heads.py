"""Merge heads

Revision ID: 4538626187a5
Revises: 232d2346208c, c531878b8bba
Create Date: 2025-02-25 21:58:46.763682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4538626187a5'
down_revision: Union[str, None] = ('232d2346208c', 'c531878b8bba')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
