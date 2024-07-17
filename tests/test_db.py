from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from fast_zero.models import User, table_registry


def test_create_user():
    engine = create_engine('sqlite:///:memory:')  # database.db | :memory:

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            username='jonas', email='jonas@local.br', password='123456'
        )

        session.add(user)
        session.commit()
        session.refresh(user)
        session.scalar(
            select(User).where(User.email == 'jonas.isaias@local.br')
        )

    assert user.id == 1
