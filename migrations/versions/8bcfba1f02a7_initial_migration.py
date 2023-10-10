"""Initial migration

Revision ID: 8bcfba1f02a7
Revises: 
Create Date: 2023-10-10 09:15:31.376520

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8bcfba1f02a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('videos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('videos',
    sa.Column('id', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('filename', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('extension', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('size', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('resolution', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('data', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='videos_pkey')
    )
    # ### end Alembic commands ###
