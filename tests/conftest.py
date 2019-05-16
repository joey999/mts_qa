import pytest
from db.manager import db_manager


@pytest.fixture(scope='session', autouse=True)
def make_restore_snapshop():
    db_manager.create_snapshot()

    yield
    db_manager.restore_from_snapshot()
    db_manager.delete_snapshot()
    return True


