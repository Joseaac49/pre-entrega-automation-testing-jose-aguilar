from utils.driver import get_driver
from utils.actions import login, add_first_product_to_cart, go_to_cart, get_cart_count
from utils.locators import CART_ITEM
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_product_to_cart():
    driver = get_driver()

    try:
        # Abrir página
        driver.get("https://www.saucedemo.com/")

        # Login
        login(driver, "standard_user", "secret_sauce")

        # Agregar producto
        add_first_product_to_cart(driver)

        # Validar contador del carrito
        cart_count = get_cart_count(driver)
        assert cart_count == "1"

        # Ir al carrito
        go_to_cart(driver)

        # Validar que el producto está en el carrito
        cart_item = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(CART_ITEM)
        )

        assert cart_item is not None
        assert cart_item.text != ""

    finally:
        # Cerrar navegador siempre
        driver.quit()