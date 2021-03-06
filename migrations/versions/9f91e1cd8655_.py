"""empty message

Revision ID: 9f91e1cd8655
Revises: 374bd75cf142
Create Date: 2017-11-24 09:04:59.463108

"""

# revision identifiers, used by Alembic.
revision = '9f91e1cd8655'
down_revision = '374bd75cf142'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('edges', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('edges', sa.Column('created_by_id', sa.Integer(), nullable=True))
    op.add_column('edges', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('edges', sa.Column('updated_by_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'edges', 'user', ['created_by_id'], ['id'])
    op.create_foreign_key(None, 'edges', 'user', ['updated_by_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'edges', type_='foreignkey')
    op.drop_constraint(None, 'edges', type_='foreignkey')
    op.drop_column('edges', 'updated_by_id')
    op.drop_column('edges', 'updated_at')
    op.drop_column('edges', 'created_by_id')
    op.drop_column('edges', 'created_at')
    # ### end Alembic commands ###
