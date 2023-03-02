"""first migration

Revision ID: 6f0547b879f5
Revises: 
Create Date: 2023-03-02 15:38:18.981386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f0547b879f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('strategy',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('creater_id', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('assignemnt', sa.ARRAY(sa.Integer()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strategy1_id', sa.String(), nullable=True),
    sa.Column('strategy2_id', sa.String(), nullable=True),
    sa.Column('result', sa.Integer(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['strategy1_id'], ['strategy.id'], ),
    sa.ForeignKeyConstraint(['strategy2_id'], ['strategy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('result')
    op.drop_table('strategy')
    # ### end Alembic commands ###