# 🍽️ Restaurante App

## 📌 Descripción

Restaurante App es una aplicación desarrollada en Python que permite administrar productos, bebidas y clientes de un restaurante mediante un menú interactivo en consola.

El proyecto fue desarrollado aplicando Programación Orientada a Objetos (POO) y los principios SOLID, utilizando una arquitectura modular para facilitar el mantenimiento y la escalabilidad del código.

---

## 🎯 Objetivos

- Aplicar Programación Orientada a Objetos.
- Implementar una estructura modular en Python.
- Aplicar los principios SOLID.
- Gestionar productos y clientes mediante un menú interactivo.
- Practicar el uso de Git y GitHub para el control de versiones.

---

## 📂 Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

---

## 💻 Funcionalidades

El sistema permite:

- Registrar productos.
- Registrar bebidas.
- Registrar clientes.
- Listar productos registrados.
- Listar clientes registrados.
- Evitar productos con códigos repetidos.
- Evitar clientes con identificaciones repetidas.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub

---

## 📖 Principios SOLID aplicados

### ✅ SRP (Single Responsibility Principle)

Cada clase tiene una única responsabilidad.

- Producto administra la información de un producto.
- Bebida extiende Producto.
- Cliente administra la información del cliente.
- Restaurante administra el registro y listado.

---

### ✅ OCP (Open/Closed Principle)

El sistema puede ampliarse creando nuevas clases que hereden de Producto sin modificar el código existente.

---

### ✅ LSP (Liskov Substitution Principle)

Las bebidas pueden utilizarse como productos gracias a la herencia y al polimorfismo.

---

## ▶️ Ejecución

Desde la carpeta del proyecto ejecutar:

```bash
python main.py
```

---

## 📋 Menú del sistema

```
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
4. Listar productos
5. Listar clientes
6. Salir
```

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica académica para la asignatura de Programación Orientada a Objetos.

Universidad Estatal Amazónica

Carrera de Tecnologías de la Información
