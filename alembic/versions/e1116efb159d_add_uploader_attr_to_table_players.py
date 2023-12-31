"""add Uploader attr to table Players

Revision ID: e1116efb159d
Revises: 7c394e8d5874
Create Date: 2023-09-16 21:16:56.023121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1116efb159d'
down_revision = '7c394e8d5874'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('players', sa.Column('uploader', sa.String(), nullable=False))
    op.create_index(op.f('ix_players_uploader'), 'players', ['uploader'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_players_uploader'), table_name='players')
    op.drop_column('players', 'uploader')
    # ### end Alembic commands ###
