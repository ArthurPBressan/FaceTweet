"""connections

Revision ID: 401bc82cc255
Revises: 2289bc7e02a7
Create Date: 2015-09-26 15:54:20.521485

"""

# revision identifiers, used by Alembic.
revision = '401bc82cc255'
down_revision = '2289bc7e02a7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('connection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('provider_id', sa.String(length=255), nullable=True),
    sa.Column('provider_user_id', sa.String(length=255), nullable=True),
    sa.Column('access_token', sa.String(length=255), nullable=True),
    sa.Column('secret', sa.String(length=255), nullable=True),
    sa.Column('display_name', sa.String(length=255), nullable=True),
    sa.Column('profile_url', sa.String(length=512), nullable=True),
    sa.Column('image_url', sa.String(length=512), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('connection')
    ### end Alembic commands ###