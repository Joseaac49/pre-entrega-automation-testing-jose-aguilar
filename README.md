# QA Automation - Saucedemo

## 📌 Descripción

Proyecto de automatización de pruebas funcionales sobre la aplicación web https://www.saucedemo.com utilizando Selenium WebDriver y Pytest.

El objetivo es validar flujos principales de usuario como login, navegación de catálogo y gestión de carrito.

---

## 🧰 Tecnologías utilizadas

* Python
* Selenium WebDriver
* Pytest
* Pytest-HTML
* Git & GitHub

---

## 🧪 Casos de prueba automatizados

### 🔐 Login

* Login exitoso con credenciales válidas
* Validación de redirección a inventory

### 📦 Inventario

* Validación del título "Products"
* Verificación de productos visibles
* Obtención de nombre y precio del primer producto

### 🛒 Carrito

* Agregado de producto al carrito
* Validación del contador
* Navegación al carrito
* Verificación de producto agregado

---

## ⚙️ Instalación

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución de tests

```bash
pytest
```

---

## 📊 Generar reporte HTML

```bash
pytest -v --html=reports/reporte.html
```

---

## 📁 Estructura del proyecto

```
tests/
utils/
reports/
```

---

## 💡 Autor

Jose Aguilar
