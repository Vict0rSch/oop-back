"""empty message

Revision ID: afdf112384be
Revises: 981588b70551
Create Date: 2017-10-30 13:09:11.677907

"""

# revision identifiers, used by Alembic.
revision = 'afdf112384be'
down_revision = '981588b70551'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

ownership = [
        ('c', 'company'),
        ('i', 'individual'),
        ('m', 'media'),
        ('o', 'other')
    ]


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('website', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('wiki', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('category', sqlalchemy_utils.types.choice.ChoiceType(ownership), nullable=True),
    sa.Column('long_name', sa.String(), nullable=True),
    sa.Column('other_groups', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('edges',
    sa.Column('child_id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('special', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['entities.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['entities.id'], ),
    sa.PrimaryKeyConstraint('child_id', 'parent_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('edges')
    op.drop_table('entities')
    # ### end Alembic commands ###
