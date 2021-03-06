"""Pitch table update

Revision ID: 22a06b9be06b
Revises: 89a68c9ca3f2
Create Date: 2021-08-14 11:16:32.563285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22a06b9be06b'
down_revision = '89a68c9ca3f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.String(), nullable=True))
    op.drop_constraint('pitches_cat_id_fkey', 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'cat_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('cat_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('pitches_cat_id_fkey', 'pitches', 'categories', ['cat_id'], ['id'])
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###
