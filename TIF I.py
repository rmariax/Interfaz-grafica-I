import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pygame




pygame.mixer.init()
ventana = tk.Tk()
ventana.title("Analisis de numeros")
ventana.geometry("500x500")
ventana.resizable(False, False)

notebook = ttk.Notebook(ventana) #se implementa notebook para correr la ventana principal como un menú y no como ventanas independientes. 
notebook.pack(pady=10, expand=True, fill="both")
#El siguiente código implementa notebook para crear una pestaña por cada ventana necesaria. 
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


def detener_musica():
    # Esta función detiene el audio
    pygame.mixer.music.stop()
    print("Música detenida a los 10 segundos.")

def reproducir_musica():
    try:
        # Cargar el archivo de música (debe estar en la misma carpeta)
        pygame.mixer.music.load("los_panchos.mp3") 
        
        # Reproducir la música (el 0 significa que se reproduce una vez)
        pygame.mixer.music.play(0)
        
        # EL TRUCO MAGNÍFICO: 
        # Le decimos a la ventana que ejecute 'detener_musica' después de 10,000 milisegundos (10s)
        ventana.after(10000, detener_musica)
        
    except pygame.error as e:
        # Si no encuentra el archivo "cancion.mp3", evitamos que el programa explote
        print(f"Error al reproducir: {e}")

    
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

tk.Label(Ficha, text= "Nombre: María Celeste Elizondo Rodríguez").place(x=5, y=15)

tk.Label(Ficha,  text= "Carnet: 2026016638").place(x=5, y=40)

tk.Label(Ficha,  text= "Edad: 19").place(x=5, y=60)

tk.Label(Ficha,  text= "Soy una estudiante de primer año de ingeniería en computadores, del TEC, me interesa la tecnología", wraplength=260, justify="left").place(x=5, y=60)

#En la siguiente línea se importan las imágenes

imagen_mapa = Image.open("mapa.png").resize((100, 100))
foto_mapa = ImageTk.PhotoImage(imagen_mapa)
tk.Label(Ficha, image=foto_mapa).place(x=280, y=15)

boton_audio = tk.Button(Ficha, text="Reproducir", command=reproducir_musica)
boton_audio.place(x=250, y=300)


ventana.mainloop()
