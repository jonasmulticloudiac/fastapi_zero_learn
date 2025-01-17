import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.models import table_registry


@pytest.fixture()
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    # gerenciamento de contexto | yield tranfora fixture em gerador
    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
