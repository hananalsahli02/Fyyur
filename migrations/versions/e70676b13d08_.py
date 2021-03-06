"""empty message

Revision ID: e70676b13d08
Revises: d9f683df884c
Create Date: 2020-05-21 12:12:04.912607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e70676b13d08'
down_revision = 'd9f683df884c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'address')
    op.add_column('Show', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.add_column('Show', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.alter_column('Show', 'start_time',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_constraint('artist_id', 'Show', type_='foreignkey')
    op.drop_constraint('venue_id', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'])
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('venue_id', 'Show', 'Venue', ['id'], ['id'])
    op.create_foreign_key('artist_id', 'Show', 'Artist', ['id'], ['id'])
    op.alter_column('Show', 'start_time',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('Show', 'venue_id')
    op.drop_column('Show', 'artist_id')
    op.add_column('Artist', sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
