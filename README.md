<h1 align="center"> Sistema de Gestión de Inventario </h1>

## 📁 Acceso al proyecto

Indica cómo se puede descargar o acceder al código fuente del proyecto, ya sea proyecto inicial o final

## 🛠️ Abre y ejecuta el proyecto

Muestra las instrucciones necesarias para abrir y ejecutar el proyecto

## :hammer: Funcionalidades del proyecto

- `Funcionalidad 1: Añadir productos`: 

Se prodrán añadir productos incluyendo nombre, precio y cantidad en cada uno, el precio debe ser un número positivo, mayor a cero y multiplo de 50 como la moneda Colombiana, y la cantidad debe ser un numero entero mayor o igual a 0; si el producto ya existe, saldrá un error y volverá a pedir la información del nuevo producto, el usuario cuenta con tres intentos para ingresar la información correctamente, si pasan los 3 intentos, sale un error y volverá al menú principal.
- `Funcionalidad 2: Consultar productos`: 

Se podrá consultar si el producto ya existe en el inventario ingresando el nombre, en caso de estar en el inventario se mostrará en pantalla el nombre, precio y cantidad de ese producto, en caso de no estar saldrá un error y volverá al menú principal.
- `Funcionalidad 3: Actualizar productos`:

Se puede actualizar un producto ingresando el nombre, si el producto existe en el inventario se pedirá el precio actualizado y la cantidad actual de producto; si el producto no existe, saldrá un error y volverá al menú principal, el precio y la cantidad que se ingrese debe cumplir con los mismos criterios que en la `funcionalidad 1`.
- `Funcionalidad 4: Eliminar productos`: 

Se podrán eliminar los productos ingresando el nombre, si el producto no está en el inventario, mostrará un error y volverá al menú principal, en caso de si estar pero la cantidad que queda de este producto es mayor a 0 entonces este no se podrá eliminar pues es necesario que este producto ya no esté disponible para que sea eliminado, de lo contrario, se eliminará satisfactoriamente.
- `Funcionalidad 5: Calcular el valor total`:

Esta funcionalidad mostrará en pantalla el valor total del inventario (la sumatoria de la multiplicación de el precio por la cantidad de cada uno de los productos)
- `Funcionalidad 6: Salir`: 

Esta es la única manera de salir del sistema, si selecciona otra opción o ingresa una opción invalida simplemente le seguirá mostrando el menú una y otra vez.
