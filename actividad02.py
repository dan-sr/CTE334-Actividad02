# -*- coding: utf-8 -*-
"""CTE-334 - Actividad 02: Distancia y dirección con interfaz gráfica."""

import tkinter as tk
from tkinter import ttk, messagebox
from math import sin, cos, sqrt, radians, asin

RADIO = 6371.0088  # radio medio de la Tierra en km


# ---------------------------------------------------------------------------
# Funciones de cálculo (Actividad 01): no dependen de widgets
# ---------------------------------------------------------------------------

def validar_coordenadas(latitud, longitud):
    """Retorna True si la latitud está entre -90 y 90 y la longitud entre -180 y 180."""
    return -90 <= latitud <= 90 and -180 <= longitud <= 180


def calcular_distancia(lat1, lon1, lat2, lon2):
    """Calcula la distancia Haversine entre dos puntos y la retorna en km."""
    phi1, phi2 = radians(lat1), radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)

    a = sin(delta_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) ** 2
    a = min(1.0, a)  # evita errores de redondeo que sacarían a 'a' de [0, 1]
    return 2 * RADIO * asin(sqrt(a))


def determinar_direccion(lat_a, lon_a, lat_b, lon_b):
    """Retorna la dirección general del punto B respecto al punto A."""
    if lat_b > lat_a:
        vertical = "Nor"
    elif lat_b < lat_a:
        vertical = "Sur"
    else:
        vertical = ""

    if lon_b > lon_a:
        horizontal = "este"
    elif lon_b < lon_a:
        horizontal = "oeste"
    else:
        horizontal = ""

    if not vertical and not horizontal:
        return "Misma ubicación"
    if not horizontal:
        return "Norte" if vertical == "Nor" else "Sur"
    if not vertical:
        return horizontal.capitalize()
    return vertical + horizontal  # Noreste, Noroeste, Sureste, Suroeste


def clasificar_distancia(distancia):
    """Clasifica la distancia (en km) según los intervalos establecidos."""
    if distancia < 1:
        return "Muy cercano"
    elif distancia < 10:
        return "Cercano"
    elif distancia < 50:
        return "Distancia media"
    return "Distante"


def formatear_resultado(distancia, direccion, clasificacion):
    """Arma el informe con el mismo formato de la Actividad 01."""
    linea = "-" * 40
    return (
        f"{linea}\n"
        "RESULTADO DEL ANÁLISIS\n"
        f"{linea}\n"
        f"Distancia: {distancia:.3f} km\n"
        f"Dirección: {direccion}\n"
        f"Clasificación: {clasificacion}\n"
        f"{linea}"
    )


# ---------------------------------------------------------------------------
# Funciones de la interfaz
# ---------------------------------------------------------------------------

def mostrar_resultado(texto):
    """Reemplaza el contenido del área de resultados por el texto recibido."""
    salida.config(state="normal")
    salida.delete("1.0", tk.END)
    salida.insert("1.0", texto)
    salida.config(state="disabled")


def ejecutar_calculo(event=None):
    """Recupera, valida y procesa los datos al presionar Calcular."""
    textos = [entrada.get() for entrada in entradas]

    try:
        lat_a, lon_a, lat_b, lon_b = [float(texto) for texto in textos]
    except ValueError:
        messagebox.showerror(
            "Entrada no numérica",
            "Todos los campos deben contener valores numéricos.",
        )
        return

    if not (validar_coordenadas(lat_a, lon_a) and validar_coordenadas(lat_b, lon_b)):
        messagebox.showerror(
            "Coordenada fuera de rango",
            "La latitud debe estar entre -90 y 90 grados y la longitud "
            "entre -180 y 180 grados.",
        )
        return

    distancia = calcular_distancia(lat_a, lon_a, lat_b, lon_b)
    direccion = determinar_direccion(lat_a, lon_a, lat_b, lon_b)
    clasificacion = clasificar_distancia(distancia)
    mostrar_resultado(formatear_resultado(distancia, direccion, clasificacion))


def limpiar():
    """Borra las cuatro entradas y el área de resultados."""
    for entrada in entradas:
        entrada.delete(0, tk.END)
    mostrar_resultado("")
    entradas[0].focus_set()


def crear_grupo_punto(contenedor, titulo, columna):
    """Crea el recuadro de un punto con sus entradas de latitud y longitud."""
    grupo = ttk.LabelFrame(contenedor, text=titulo, padding=10)
    grupo.grid(row=0, column=columna, padx=5, sticky="nsew")

    ttk.Label(grupo, text="Latitud").grid(row=0, column=0, sticky="w", pady=3)
    latitud = ttk.Entry(grupo, width=16)
    latitud.grid(row=0, column=1, padx=(8, 0), pady=3)

    ttk.Label(grupo, text="Longitud").grid(row=1, column=0, sticky="w", pady=3)
    longitud = ttk.Entry(grupo, width=16)
    longitud.grid(row=1, column=1, padx=(8, 0), pady=3)

    return latitud, longitud


# ---------------------------------------------------------------------------
# Construcción de la ventana
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("CTE-334 - Análisis entre dos puntos geográficos")
    ventana.resizable(False, False)

    principal = ttk.Frame(ventana, padding=15)
    principal.grid(row=0, column=0)

    ttk.Label(
        principal,
        text="CTE-334  Análisis entre dos puntos geográficos",
        font=("TkDefaultFont", 13, "bold"),
    ).grid(row=0, column=0, pady=(0, 4))

    ttk.Label(principal, text="Ingrese las coordenadas en grados decimales").grid(
        row=1, column=0, pady=(0, 8)
    )

    puntos = ttk.Frame(principal)
    puntos.grid(row=2, column=0)
    lat_a_entry, lon_a_entry = crear_grupo_punto(puntos, "Punto A", 0)
    lat_b_entry, lon_b_entry = crear_grupo_punto(puntos, "Punto B", 1)
    entradas = [lat_a_entry, lon_a_entry, lat_b_entry, lon_b_entry]

    botones = ttk.Frame(principal)
    botones.grid(row=3, column=0, pady=10)
    ttk.Button(botones, text="Calcular", command=ejecutar_calculo).grid(row=0, column=0, padx=5)
    ttk.Button(botones, text="Limpiar", command=limpiar).grid(row=0, column=1, padx=5)

    marco_resultado = ttk.LabelFrame(principal, text="Resultado", padding=8)
    marco_resultado.grid(row=4, column=0, sticky="ew")
    salida = tk.Text(marco_resultado, width=44, height=7, font="TkFixedFont", state="disabled")
    salida.grid(row=0, column=0, sticky="ew")
    marco_resultado.columnconfigure(0, weight=1)

    ventana.bind("<Return>", ejecutar_calculo)
    lat_a_entry.focus_set()

    ventana.mainloop()
