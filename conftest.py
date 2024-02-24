import pytest
from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        # Проверка на наличие фикстуры и, если её нет, создание заново
        practice_form_page = fixture.open_practice_form_page()
        practice_form_page.open_site()

    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    yield fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request, app):
    yield app

