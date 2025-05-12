<h1 align="center"> Sistema de Gestión de Inventario </h1>

## 📁 Acceso y ejecución del proyecto

1. Descarga Python [aquí](https://www.python.org/downloads/).

Da click en el sistema operativo de tu computador y descarga el _Latest release_, luego simplemente sigue el paso a paso del descargable.

![imagen](https://github.com/user-attachments/assets/d037aaff-2adb-42f1-a512-a118adf4a04a)
![imagen](https://github.com/user-attachments/assets/5c802e84-cee0-4a81-81ed-725cc447a58c)

2. Descargamos el archivo `.py`.

![imagen](https://github.com/user-attachments/assets/9def2f5c-4b6b-4807-91c4-94fa3a9c1ad3)![imagen](https://github.com/user-attachments/assets/2cd09504-db58-4c61-a223-0f3944139117)



3. Abrimos la terminal del computador.

![imagen](https://github.com/user-attachments/assets/8d36087b-131e-4bc6-a256-1edd8274637e)

4. Búscamos la carpeta en la que descargamos el archivo `.py`.
- Usa `ls` para visualizar los archivos y carpetas que se encuentran donde estas situado.
- Usa `cd` para ingresar a la carpeta que necesites.

En este caso está dentro de la carpeta Prueba, que está dentro de la carpeta Susana:

![imagen](https://github.com/user-attachments/assets/9be747a3-3a58-4b47-995a-fef941f356d2)

5. Luego ejecutamos el proyecto usando `python3` y el nombre del ejecutable, como se muestra a continuación:

![imagen](https://github.com/user-attachments/assets/4af8fa98-8a12-464e-ab33-5a744a443752)


## :hammer: Funcionalidades del proyecto

- `Funcionalidad 1: Añadir productos`: 

Se prodrán añadir productos incluyendo nombre, precio y cantidad en cada uno, el precio debe ser un número positivo, mayor a cero y multiplo de 50 como la moneda Colombiana, y la cantidad debe ser un numero entero mayor o igual a 0; si el producto ya existe, saldrá un error y volverá a pedir la información del nuevo producto, el usuario cuenta con tres intentos para ingresar la información correctamente, si pasan los 3 intentos, sale un error y volverá al menú principal.

![imagen](https://github.com/user-attachments/assets/287621b5-4889-4875-ac71-a96e2c778eb7)

- `Funcionalidad 2: Consultar productos`: 

Se podrá consultar si el producto ya existe en el inventario ingresando el nombre, en caso de estar en el inventario se mostrará en pantalla el nombre, precio y cantidad de ese producto, en caso de no estar saldrá un error y volverá al menú principal.

![imagen](https://github.com/user-attachments/assets/365c6d40-f307-41c5-9bd2-41e3533f3b5e)![imagen](https://github.com/user-attachments/assets/95d69276-38d3-4064-bc23-827a0618fb43)

- `Funcionalidad 3: Actualizar productos`:

Se puede actualizar un producto ingresando el nombre, si el producto existe en el inventario se pedirá el precio actualizado y la cantidad actual de producto; si el producto no existe, saldrá un error y volverá al menú principal, el precio y la cantidad que se ingrese debe cumplir con los mismos criterios que en la `funcionalidad 1`.

![imagen](https://github.com/user-attachments/assets/35dda9c8-7565-4dd6-9889-113f0ae46216)

- `Funcionalidad 4: Eliminar productos`: 

Se podrán eliminar los productos ingresando el nombre, si el producto no está en el inventario, mostrará un error y volverá al menú principal, en caso de si estar pero la cantidad que queda de este producto es mayor a 0 entonces este no se podrá eliminar pues es necesario que este producto ya no esté disponible para que sea eliminado, de lo contrario, se eliminará satisfactoriamente.

![imagen](https://github.com/user-attachments/assets/ee91dfcb-bb6b-4022-9557-4fc8a89226d7)![imagen](https://github.com/user-attachments/assets/78f060ce-52ac-48be-bf75-0bc2d81cbed8)


- `Funcionalidad 5: Calcular el valor total`:

Esta funcionalidad mostrará en pantalla el valor total del inventario (la sumatoria de la multiplicación de el precio por la cantidad de cada uno de los productos)

![imagen](https://github.com/user-attachments/assets/01c7d31e-8684-447e-9e28-ecc3c35eaeb7)

- `Funcionalidad 6: Salir`: 

Esta es la única manera de salir del sistema, si selecciona otra opción o ingresa una opción invalida simplemente le seguirá mostrando el menú una y otra vez.

![imagen](https://github.com/user-attachments/assets/50072875-d87b-4dc5-86e5-a74c9917f137)![imagen](https://github.com/user-attachments/assets/7eac3704-8ece-4496-bf7f-76b419239314)

