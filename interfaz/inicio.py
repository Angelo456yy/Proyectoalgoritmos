import tkinter as tk
import subprocess
from PIL import Image, ImageTk
import pygame



# Resto del código
def reproducir_musica():
    pygame.mixer.init()  # Inicializa el módulo de sonido de pygame
    pygame.mixer.music.load(r"C:\Users\al881\OneDrive\Escritorio\Proyecto algoritmos\interfaz\song.mp3")  # Reemplaza "cancion.mp3" con la ubicación de tu archivo de música
    pygame.mixer.music.play()

def on_button1_click():
    try:
        # Reemplaza "programa.py" con el nombre de tu programa Python.
        programa = "interfazinve.py"
        subprocess.run(["python", programa], check=True)
        label.config(text="¡El programa se ejecutó con éxito!")
    except subprocess.CalledProcessError:
        label.config(text="¡Error al ejecutar el programa!")

def on_button2_click():
    try:
        # Reemplaza "programa.py" con el nombre de tu programa Python.
        programa = "interfaclientes.py"
        subprocess.run(["python", programa], check=True)
        label.config(text="¡El programa se ejecutó con éxito!")
    except subprocess.CalledProcessError:
        label.config(text="¡Error al ejecutar el programa!")

def on_button3_click():
    try:
        # Reemplaza "programa.py" con el nombre de tu programa Python.
        programa = "ventasinterfa.py"
        subprocess.run(["python", programa], check=True)
        label.config(text="¡El programa se ejecutó con éxito!")
    except subprocess.CalledProcessError:
        label.config(text="¡Error al ejecutar el programa!")


def on_button4_click():
    try:
        # Reemplaza "programa.py" con el nombre de tu programa Python.
        programa = "reporfas.py"
        subprocess.run(["python", programa], check=True)
        label.config(text="¡El programa se ejecutó con éxito!")
    except subprocess.CalledProcessError:
        label.config(text="¡Error al ejecutar el programa!")
        
        
def anuncio():
    try:
        # Reemplaza "programa.py" con el nombre de tu programa Python.
        programa = r"C:\Users\al881\OneDrive\Escritorio\Proyecto algoritmos\interfaz\anuncios.py"
        subprocess.run(["python", programa], check=True)
        label.config(text="¡El programa se ejecutó con éxito!")
    except subprocess.CalledProcessError:
        label.config(text="¡Error al ejecutar el programa!")        
    
    
ventana = tk.Tk()
ventana.geometry('500x300')
ventana.config(bg='#262727')
ventana.title('PROGRAMA PRO')
ventana.iconbitmap(r'C:\Users\al881\OneDrive\Escritorio\Proyecto algoritmos\interfaz\inicios.ico')

label = tk.Label(ventana, text="Bienvenido",width=40,font=("Helvetica", 20, "bold"),bg="#2f3136", fg="white", borderwidth=2)
label.pack(padx=10, pady=10)  # Ajusta los valores según la separación deseada

button1 = tk.Button(ventana, text="Inventario", relief=tk.SOLID, command=on_button1_click, bg="#8c14dc", fg="white", borderwidth=2)
button1.pack(padx=10, pady=10, anchor="w") # Ajusta los valores según la separación deseada

button2 = tk.Button(ventana, text="Control de clientes", command=on_button2_click,  relief=tk.SOLID, bg="#8c14dc", fg="white", borderwidth=2)
button2.pack(padx=10, pady=10, anchor="w")  # Ajusta los valores según la separación deseada

button3= tk.Button(ventana, text="Control de ventas", command=on_button3_click,bg="#8c14dc", fg="white",  relief=tk.SOLID, borderwidth=2)
button3.pack(padx=10, pady=10, anchor="w")

button4 = tk.Button(ventana, text="Reportes", command=on_button4_click, bg="#8c14dc", fg="white",  relief=tk.SOLID, borderwidth=2)
button4.pack(padx=10, pady=10, anchor="w")

reproducir_button = tk.Button(ventana, text="Reproducir Música", command=reproducir_musica,relief=tk.SOLID, bg="#8c14dc", fg="white", borderwidth=2)
reproducir_button.pack(side="left", padx=10, pady=10)


anuncio = tk.Button(ventana, text="anuncio",relief=tk.SOLID, bg="#8c14dc", fg="white", command=anuncio, borderwidth=2)
anuncio.pack(side="left",padx=10, pady=10)

# Abre el archivo de imagen GIF
imagen = Image.open(r"C:\Users\al881\OneDrive\Escritorio\Proyecto algoritmos\interfaz\6761127.jpg")

# Convierte la imagen en un objeto Tkinter PhotoImage
imagen_tk = ImageTk.PhotoImage(imagen)

# Crea una etiqueta para mostrar la imagen
etiqueta = tk.Label(ventana, image=imagen_tk)
etiqueta.pack()



ventana.mainloop()






