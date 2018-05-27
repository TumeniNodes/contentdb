"""empty message

Revision ID: 4e482c47e519
Revises: 900758871713
Create Date: 2018-05-27 22:38:16.507155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e482c47e519'
down_revision = '900758871713'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dependency',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('depender_id', sa.Integer(), nullable=True),
    sa.Column('package_id', sa.Integer(), nullable=True),
    sa.Column('meta_package_id', sa.Integer(), nullable=True),
    sa.Column('optional', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['depender_id'], ['package.id'], ),
    sa.ForeignKeyConstraint(['meta_package_id'], ['meta_package.id'], ),
    sa.ForeignKeyConstraint(['package_id'], ['package.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('depender_id', 'package_id', 'meta_package_id', name='_dependency_uc')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dependency')
    # ### end Alembic commands ###
