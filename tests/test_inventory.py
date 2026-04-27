from utils.driver import get_driver
from utils.actions import login, get_products
from utils.locators import PRODUCT_TITLE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inventory_page():
    driver = get_driver()

    driver.get("https://www.saucedemo.com/")
    login(driver, "standard_user", "secret_sauce")

    # Validar título
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PRODUCT_TITLE)
    )
    assert title.text == "Products"

    # Validar que hay productos
    products = get_products(driver)
    assert len(products) > 0

    # Obtener info del primer producto
    first_product = products[0]
    product_name = first_product.find_element("class name", "inventory_item_name").text
    product_price = first_product.find_element("class name", "inventory_item_price").text

    print(f"Producto: {product_name} - Precio: {product_price}")

    driver.quit()

    assert product_name != ""
    assert "$" in product_price