# Código de elmentos finitos

Para compilar y ejecutar este código hace falta tener *python3* con las librerías de *numpy* 
y *matlplotlib* instaladas.

En el archivo main se encuentra la definición de la ecuación en derivadas parciales que se quiera comprobar, junto con las condiciones de contorno.

Dentro de las carpeta Domain se encuentra el código necesario para la generación de la malla, en Controller los algoritmos y procedimientos necesarios para la resolución del MEF y el ensamblaje, y finalmente en la carpeta View el código para mostrar la solución en un gráfica.

## Instalar dependencias

`pip3 install numpy`

`pip3 install matplotlib`

## Ejecutar

`python3 main.py`