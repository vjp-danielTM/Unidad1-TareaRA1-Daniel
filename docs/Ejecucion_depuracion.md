# EJECUCION Y DEPURACION DEL CODIGO

Lo primero que  hice fue hacer un `tree` para ver  que  tenia en mi repositorio y localizar el `main_app.py`.

![Tree del repo](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/ejecucion_depuracion_img/1.png)


Ahora lo que voy es a crear un entorno virtual controlado llamado lavadero con:

> `python3 -m venv lavadero` 

Que sirve para ejecutar entornos de python sin dañar a los demas proyectos que tengo.

Una vez creado lo tengo que activar con el comando:
> `source lavadero/bin/activate` 

simplemente con esto ya estaria activado y se puede ver porque al principio de la shell aparece el nombre del entorno `(lavadero)`.

![Entorno controlado](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/ejecucion_depuracion_img/2.png)


Ahora quedaria ejecutar el codigo:
> `PYTHONPATH=src python3 src/main_app.py`

Con este codigo lo ejecutamos pero que es lo que hay en el codigo exactamente.

`PYTHONPATH=src` Con este le estoy diciendo que coja como raiz la carpeta src que es donde tengo los .py a ejecutar.

`python3 src/main_app.py` con esto se ejecuta el archivo principal de la aplicación que es `main_app.py`, que está dentro de `src/`.

![Ejecucion y depuracion del codigo](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/ejecucion_depuracion_img/3.png)

![Ejecucion y depuracion del codigo](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/ejecucion_depuracion_img/4.png)

Como vemos al final de la ejecucion nos indica que hay un fallo en la linea 83.

Ahora o con `nano main_app.py` como yo hice en el ejemplo o desde visual code vamos a la linea 83 y vemos que el fallo es que no se indica encerado a False como pone en el enunciado del ejemplo 4.

![Ejecucion y depuracion del codigo](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/ejecucion_depuracion_img/5.png)

Y vemos que ahora todos los ejemplos salen con los resultados que buscabamos.

![Ejecucion Final del codigo](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/ejecucion_depuracion_img/6.png)
![Ejecucion Final del codigo](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/ejecucion_depuracion_img/7.png)
![Ejecucion Final del codigo](https://raw.githubusercontent.com/vjp-danielTM/Unidad1-TareaRA1-Daniel/refs/heads/main/docs/ejecucion_depuracion_img/8.png)
