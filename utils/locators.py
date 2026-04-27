from selenium.webdriver.common.by import By

# LOGIN
USERNAME_INPUT = (By.ID, "user-name")
PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")

# INVENTORY
PRODUCT_TITLE = (By.CLASS_NAME, "title")
INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

# CARRITO
ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

# PRODUCTO EN CARRITO
CART_ITEM = (By.CLASS_NAME, "inventory_item_name")