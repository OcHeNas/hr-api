"""Added account table

Revision ID: cfcf629d8da0
Revises: 
Create Date: 2024-03-21 15:48:35.940983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cfcf629d8da0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vacancy',
    sa.Column('id_vacancy', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=False),
    sa.Column('Post', sa.VARCHAR(length=50), nullable=False),
    sa.Column('Description', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id_vacancy')
    )
    op.create_table('applicant',
    sa.Column('id_applicant', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('FIO', sa.VARCHAR(length=50), nullable=False),
    sa.Column('Passport', sa.TEXT(), nullable=False),
    sa.Column('INN', sa.VARCHAR(length=12), nullable=False),
    sa.Column('Birthday', sa.Date(), nullable=False),
    sa.Column('Gender', sa.VARCHAR(length=50), nullable=False),
    sa.Column('Address', sa.VARCHAR(length=100), nullable=False),
    sa.Column('Resume', sa.TEXT(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), nullable=False),
    sa.Column('id_vacancy', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_vacancy'], ['vacancy.id_vacancy'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_applicant')
    )
    op.create_table('department',
    sa.Column('id_department', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('Description', sa.TEXT(), nullable=False),
    sa.Column('id_director', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_department')
    )
    op.create_table('post',
    sa.Column('id_post', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Members', sa.Integer(), nullable=False),
    sa.Column('Salary', sa.Integer(), nullable=False),
    sa.Column('Name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id_department'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_post')
    )
    op.create_table('order',
    sa.Column('id_order', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Type', sa.VARCHAR(length=100), nullable=False),
    sa.Column('Date', sa.Date(), nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id_post'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_order')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('permissions', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('FIO', sa.VARCHAR(length=50), nullable=False),
    sa.Column('username', sa.VARCHAR(length=10), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('Passport', sa.TEXT(), nullable=False),
    sa.Column('INN', sa.VARCHAR(length=12), nullable=False),
    sa.Column('Birthday', sa.Date(), nullable=False),
    sa.Column('Gender', sa.VARCHAR(length=50), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('role_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('department', sa.Integer(), nullable=True),
    sa.Column('email', sa.VARCHAR(length=50), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['department'], ['department.id_department'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id_order'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('order')
    op.drop_table('post')
    op.drop_table('department')
    op.drop_table('applicant')
    op.drop_table('vacancy')
    # ### end Alembic commands ###
