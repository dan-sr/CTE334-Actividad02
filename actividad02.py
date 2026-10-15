# -*- coding: utf-8 -*-
"""CTE-334 - Actividad 02: Distancia y dirección con interfaz gráfica."""

import tkinter as tk
from tkinter import ttk

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
    pass  # pendiente: conectar con los cálculos


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
