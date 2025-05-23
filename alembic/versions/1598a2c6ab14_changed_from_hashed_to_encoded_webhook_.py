"""Changed from hashed to encoded webhook secret

Revision ID: 1598a2c6ab14
Revises: 7a216572a792
Create Date: 2025-05-17 10:27:51.288021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1598a2c6ab14'
down_revision: Union[str, None] = '7a216572a792'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('webhooks', sa.Column('encoded_webhook_secret', sa.String(), nullable=False, server_default=""))
    op.drop_column('webhooks', 'hashed_webhook_secret')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('webhooks', sa.Column('hashed_webhook_secret', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('webhooks', 'encoded_webhook_secret')
    # ### end Alembic commands ###
