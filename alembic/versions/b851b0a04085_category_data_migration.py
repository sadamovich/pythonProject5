"""category data migration

Revision ID: b851b0a04085
Revises: 8dd9d7adff7f
Create Date: 2023-07-11 12:45:55.178394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b851b0a04085'
down_revision = '8dd9d7adff7f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            'category',
            sa.column('name', sa.VARCHAR(64)),
            sa.column('slug', sa.VARCHAR(64)),
        ),
        [
            {'name': 'Beginner', 'slug': 'beginner'},
            {'name': 'Expert', 'slug': 'expert'}
        ]
    )


def downgrade() -> None:
    pass
