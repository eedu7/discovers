"""fixed the default value of the uuid4

Revision ID: dc3c515bd776
Revises: 9a960015f496
Create Date: 2025-07-08 18:39:16.308071

"""

from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "dc3c515bd776"
down_revision: Union[str, Sequence[str], None] = "9a960015f496"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
