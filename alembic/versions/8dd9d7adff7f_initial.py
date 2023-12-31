"""initial

Revision ID: 8dd9d7adff7f
Revises: 
Create Date: 2023-07-11 12:44:52.326193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dd9d7adff7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('slug', sa.VARCHAR(length=64), nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_name'), 'category', ['name'], unique=True)
    op.create_index(op.f('ix_category_slug'), 'category', ['slug'], unique=True)
    op.create_table('runner',
    sa.Column('name', sa.VARCHAR(length=32), nullable=False),
    sa.Column('surname', sa.VARCHAR(length=32), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('category_id', sa.INTEGER(), nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('runner')
    op.drop_index(op.f('ix_category_slug'), table_name='category')
    op.drop_index(op.f('ix_category_name'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###
