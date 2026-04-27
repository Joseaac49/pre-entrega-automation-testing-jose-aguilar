from utils.driver import get_driver
from utils.actions import login

def test_login_success():
    driver = get_driver()

    driver.get("https://www.saucedemo.com/")

    login(driver, "standard_user", "secret_sauce")

    # Validación
    assert "inventory.html" in driver.current_url

    driver.quit()

