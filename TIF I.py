import tkinter as tk
from tkinter import ttk




ventana = tk.Tk()
ventana.title("Analisis de numeros")
ventana.geometry("500x500")
ventana.resizable(False, False)

notebook = ttk.Notebook(ventana)
notebook.pack(pady=10, expand=True, fill="both")
Analisis_numeros = tk.Frame(notebook)
Ficha = tk.Frame(notebook)
Animacion = tk.Frame(notebook)
notebook.add(Analisis_numeros, text="Análisis Númerico")
notebook.add(Ficha, text="Ficha Informativa")
notebook.add(Animacion, text="Animación")


def cerrarVentana():
    ventana.destroy()

def encontrar_pares(n, a=1, resultado=None):
    if resultado is None:
        resultado = []
    if a * a > n: 
        return resultado
    if n % a == 0: 
        resultado.append((a, n // a))
    return encontrar_pares(n, a + 1, resultado)

def analaizar(): 
    n = int(entry.get())
    pares = encontrar_pares(n)
    resultado_label.config(text=f"Pares: {pares}")

    
canva1 = tk.Canvas(Analisis_numeros, bg="pink" , width=500, height=500)
canva1.pack(expand=True, fill="both")


label = tk.Label(canva1, text="Ingrese un numero entero:", bg="pink")
label.place(x=125, y=150)

entry = tk.Entry(canva1)
entry.place(x=130, y=200)

resultado_label = tk.Label(canva1, text="", bg="pink")
resultado_label.place(x=190, y=300)




boton_probar = tk.Button(canva1, text="Analizar", command=analaizar)
boton_probar.place(x=150, y=250)



boton_cerrar = tk.Button(canva1, text="Cerrar" , command=cerrarVentana)
boton_cerrar.place(x=190,y=20)

#Punto 2 
Informacion = tk.Label(Ficha, text="Sobre mí")


ventana.mainloop()
