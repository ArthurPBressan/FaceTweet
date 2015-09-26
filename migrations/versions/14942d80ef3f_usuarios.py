"""Usuarios

Revision ID: 14942d80ef3f
Revises: None
Create Date: 2015-09-26 12:47:56.359977

"""

# revision identifiers, used by Alembic.
revision = '14942d80ef3f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=80), nullable=True),
    sa.Column('descricao', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('senha', sa.String(length=255), nullable=True),
    sa.Column('ativo', sa.Boolean(), nullable=True),
    sa.Column('confirmado', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('roles_usuarios',
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_usuarios')
    op.drop_table('usuario')
    op.drop_table('role')
    ### end Alembic commands ###
