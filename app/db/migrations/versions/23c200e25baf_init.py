"""init

Revision ID: 23c200e25baf
Revises: 
Create Date: 2024-03-08 20:51:50.817797

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "23c200e25baf"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "items",
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.VARCHAR(length=256), nullable=True),
        sa.Column("price", sa.NUMERIC(precision=16, scale=2), nullable=True),
        sa.PrimaryKeyConstraint("item_id"),
    )
    op.create_table(
        "users",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("username", sa.VARCHAR(length=256), nullable=True),
        sa.PrimaryKeyConstraint("user_id"),
    )
    op.create_table(
        "orders",
        sa.Column("order_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("item_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["item_id"], ["items.item_id"], onupdate="RESTRICT", ondelete="RESTRICT"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.user_id"], onupdate="RESTRICT", ondelete="RESTRICT"
        ),
        sa.PrimaryKeyConstraint("order_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("orders")
    op.drop_table("users")
    op.drop_table("items")
    # ### end Alembic commands ###
