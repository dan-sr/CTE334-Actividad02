# CTE-334 - Actividad 02: Distancia y dirección con interfaz gráfica

**Estudiante:** Daniel Sierra
**Número de cuenta:** 20201004160

## Propósito
Aplicación de escritorio en Python que convierte el programa de la Actividad 01 en una
interfaz gráfica con Tkinter y ttk. Recibe las coordenadas de los puntos A y B, valida los
datos, muestra ventanas emergentes cuando encuentra errores y presenta dentro de la ventana
la distancia (Haversine), la dirección general de B respecto a A y la clasificación de la distancia.

## Versión de Python y ejecución
- Python 3.12 (funciona con Python 3.6 o superior que incluya Tkinter).
- Solo usa la biblioteca estándar: `tkinter`, `tkinter.ttk`, `tkinter.messagebox` y `math`.
- Ejecutar desde la consola:

```
python actividad02.py
```

## Controles de la interfaz
- **Punto A / Punto B:** dos recuadros, cada uno con una caja de entrada para la latitud y otra para la longitud, en grados decimales.
- **Calcular:** ejecuta `ejecutar_calculo()`, que recupera los cuatro valores, los valida y muestra el resultado. También se activa con la tecla Enter.
- **Limpiar:** borra las cuatro entradas y el área de resultado.
- **Resultado:** área de texto de solo lectura donde aparece el informe con el formato de la Actividad 01. Cada cálculo reemplaza el anterior.

## Funciones
- `validar_coordenadas()`, `calcular_distancia()`, `determinar_direccion()` y `clasificar_distancia()`: las mismas de la Actividad 01. No usan widgets ni ventanas emergentes.
- `formatear_resultado()`: arma el texto del informe.
- `ejecutar_calculo()`: callback del botón Calcular. Usa `get()`, convierte a `float` dentro de `try/except`, valida los rangos y llama a las funciones de cálculo.
- `mostrar_resultado()`: borra el Text con `delete('1.0', tk.END)` y escribe el informe con `insert()`.
- `limpiar()` y `crear_grupo_punto()`: limpian el formulario y construyen los recuadros de cada punto.

## Caso propio (sitios reales de Honduras)
Nombre del sitio A: Tegucigalpa
Coordenadas: 14.0723, -87.1921

Nombre del sitio B: La Ceiba
Coordenadas: 15.7597, -86.7822

Distancia obtenida: 192.730 km
Dirección obtenida: Noreste
Clasificación obtenida: Distante

## Pruebas realizadas
| Caso | Entradas | Resultado obtenido |
|---|---|---|
| A | Tegucigalpa (14.0723, -87.1921) y Comayagua (14.4514, -87.6375) | 63.882 km; Noroeste; Distante |
| B | Dos puntos idénticos (14.0723, -87.1921) | 0.000 km; Misma ubicación; Muy cercano |
| C | Latitud A vacía / Latitud A = `abc` | Ventana "Entrada no numérica" |
| D | Latitud A = 97.5 | Ventana "Coordenada fuera de rango" |
| E | Longitud A = -185 | Ventana "Coordenada fuera de rango" |
| F | Tegucigalpa y La Ceiba | 192.730 km; Noreste; Distante |
| Frontera | A (-90, -180), B (90, 180) | Valores aceptados: 20015.114 km; Noreste; Distante |

Después de cada ventana de error la aplicación sigue abierta, se pueden corregir los campos
y el resultado anterior no se modifica.

## Decisiones de interfaz
Configuré el área de resultado (`tk.Text`) como solo lectura (`state="disabled"`) para que el
usuario no pueda escribir en ella por accidente ni modificar un resultado. Por eso,
`mostrar_resultado()` la habilita solo un momento, borra el contenido anterior, inserta el
informe nuevo y la vuelve a deshabilitar. También usé un único gestor, `grid()`, en todos los
contenedores para evitar mezclarlo con `pack()`, y la fuente `TkFixedFont` para que las líneas
de guiones queden alineadas en cualquier computadora.
