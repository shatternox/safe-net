"""empty message

Revision ID: 7b9fbb89b3bf
Revises: 
Create Date: 2021-03-25 22:01:42.184859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b9fbb89b3bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('log', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('client_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log')
    # ### end Alembic commands ###
