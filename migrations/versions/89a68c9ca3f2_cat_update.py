"""cat update

Revision ID: 89a68c9ca3f2
Revises: cc413aeafbbc
Create Date: 2021-08-14 03:24:57.572001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89a68c9ca3f2'
down_revision = 'cc413aeafbbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('category_title', sa.String(), nullable=True))
    op.drop_column('categories', 'categories_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('categories_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('categories', 'category_title')
    # ### end Alembic commands ###
