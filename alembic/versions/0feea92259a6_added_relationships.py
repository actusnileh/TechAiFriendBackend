"""Added relationships

Revision ID: 0feea92259a6
Revises: 4b27a083cb2c
Create Date: 2024-09-21 13:25:40.773868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0feea92259a6'
down_revision: Union[str, None] = '4b27a083cb2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('friends', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'friends', 'users', ['user_id'], ['vk_id'])
    op.add_column('groups', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'groups', 'users', ['user_id'], ['vk_id'])
    op.add_column('photo', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'photo', 'users', ['user_id'], ['vk_id'])
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['vk_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    op.drop_constraint(None, 'photo', type_='foreignkey')
    op.drop_column('photo', 'user_id')
    op.drop_constraint(None, 'groups', type_='foreignkey')
    op.drop_column('groups', 'user_id')
    op.drop_constraint(None, 'friends', type_='foreignkey')
    op.drop_column('friends', 'user_id')
    # ### end Alembic commands ###
