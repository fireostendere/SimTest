import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
        # Проверка на наличие фикстуры и, если её нет, создание заново
        practice_form_page = fixture.open_practice_form_page()
        practice_form_page.open_site()
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
