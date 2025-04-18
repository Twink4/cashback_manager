"""Added Coliumn Mcc_code

Revision ID: 63b429c493fe
Revises: cae8fc3b4e7d
Create Date: 2025-04-06 21:26:33.328600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63b429c493fe'
down_revision: Union[str, None] = 'cae8fc3b4e7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mcc_codes', sa.Column('mcc_code', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'mcc_codes', ['mcc_code'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mcc_codes', type_='unique')
    op.drop_column('mcc_codes', 'mcc_code')
    # ### end Alembic commands ###
