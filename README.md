# CTE-334 - Actividad 02: Distancia y dirección con interfaz gráfica

**Estudiante:** Daniel Sierra
**Número de cuenta:** 20201004160

¿Para qué sirve?

Esta aplicación calcula la distancia entre dos puntos de la Tierra. Tú escribes la latitud y la longitud de cada punto, y el programa te muestra:

La distancia entre los dos puntos.
La dirección en la que está el punto B, visto desde el punto A.
Qué tan lejos están (muy cercano, cercano, distante, etc.).
Versión de Python y cómo ejecutarlo
Versión usada: Python 3.12. También funciona con Python 3.6 o superior que tenga Tkinter.
No necesita instalar nada más, porque solo usa herramientas que ya vienen con Python.

Para ejecutarlo, escribe en la consola:

python actividad02.py
Controles de la interfaz
Punto A y Punto B: cada uno tiene dos cajas para escribir la latitud y la longitud, en grados decimales.
Calcular: revisa los datos y muestra el resultado. También puedes presionar la tecla Enter.
Limpiar: borra todas las cajas y el resultado.
Área de resultado: aquí aparece el informe. Solo se puede leer, no escribir. Cada cálculo nuevo reemplaza al anterior.
Caso propio: Tegucigalpa y La Ceiba
Tegucigalpa: latitud 14.0723, longitud -87.1921
La Ceiba: latitud 15.7597, longitud -86.7822

Resultado:

Distancia: 192.730 km
Dirección: Noreste
Clasificación: Distante
Pruebas realizadas
Caso	Qué se probó	Resultado
A	Tegucigalpa y Comayagua	63.882 km, Noroeste, Distante
B	Dos puntos iguales	0.000 km, Misma ubicación, Muy cercano
C	Latitud de A vacía o con “abc”	Ventana “Entrada no numérica”
D	Latitud de A = 97.5	Ventana “Coordenada fuera de rango”
E	Longitud de A = -185	Ventana “Coordenada fuera de rango”
F	Tegucigalpa y La Ceiba	192.730 km, Noreste, Distante
Límite	A (-90, -180) y B (90, 180)	20015.114 km, Noreste, Distante

Después de cada error, la aplicación sigue abierta. Puedes corregir los datos y volver a calcular. El resultado anterior no cambia hasta que hagas un cálculo correcto.Decisiones de interfaz

Decidí que el área de resultado sea de solo lectura. Así nadie puede cambiar el informe por accidente. Cuando hay un cálculo nuevo, la aplicación desbloquea el área un momento, borra lo anterior, escribe el resultado nuevo y la vuelve a bloquear. También usé una letra de ancho fijo para que las líneas de guiones se vean derechas en cualquier computadora.
