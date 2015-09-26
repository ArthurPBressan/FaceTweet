"""connection full name

Revision ID: e1855559096
Revises: 401bc82cc255
Create Date: 2015-09-26 17:40:20.742180

"""

# revision identifiers, used by Alembic.
revision = 'e1855559096'
down_revision = '401bc82cc255'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('connection', sa.Column('full_name', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('connection', 'full_name')
    ### end Alembic commands ###