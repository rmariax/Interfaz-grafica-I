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

tk.Label(Ficha,  text= "Soy una estudiante de primer año de ingeniería en computadores, del TEC. Me gusta la programación, sin embargo, tengo preferencias en el área de electrónica.", wraplength=260, justify="left").place(x=5, y=60)

#En la siguiente línea se importan las imágenes y los encabezados correspondientes. 

tk.Label(Ficha, text= "Imagen de la programadora").place(x=300, y=15)
tk.Label(Ficha, text="Mapa del lugar donde vive:").place(x=0, y=160)

imagen_programadora = Image.open("programadora.png").resize((100, 100))
foto_programadora = ImageTk.PhotoImage(imagen_programadora)
tk.Label(Ficha, image=foto_programadora).place(x=320, y=40)

imagen_mapa = Image.open("mapa.png").resize((150, 150))
foto_mapa = ImageTk.PhotoImage(imagen_mapa)
tk.Label(Ficha, image=foto_mapa).place(x=0, y=200)


#en la siguiente línea se agrega la inforomación sobre el grupo Musical. 
tk.Label(Ficha, text="Información del grupo Musical").place(x=280, y=180)
tk.Label(Ficha, text="Los Panchos, género Bolero Romántico.").place(x=280, y=200)

imagen_grupo = Image.open("lospanchos.png").resize((150, 150))
foto_panchos = ImageTk.PhotoImage(imagen_grupo)
tk.Label(Ficha, image=foto_panchos).place(x=280, y=230)

boton_audio = tk.Button(Ficha, text="Reproducir", command=reproducir_musica)
boton_audio.place(x=320, y=390)

#Sección 3, Animación 

canva3 = tk.Canvas(Animacion, bg="black", width=500, height=400)
canva3.pack()

# control de velocidad
frame_control = tk.Frame(Animacion, bg="white")
frame_control.pack(pady=5)

# Etiqueta deslizable para la velocidad

tk.Label(frame_control, text="Velocidad:", bg="white").pack(side="left")
velocidad_slider = tk.Scale(frame_control, from_=1, to=10, orient="horizontal")
velocidad_slider.set(3)
velocidad_slider.pack(side="left")









ventana.mainloop()
