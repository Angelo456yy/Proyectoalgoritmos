import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Anuncio")
ventana.iconbitmap(r'C:\Users\al881\OneDrive\Escritorio\Proyecto algoritmos\interfaz\inicios.ico')

# Cargar la imagen y convertirla a un formato compatible con tkinter
imagen = Image.open(r"C:\Users\al881\OneDrive\Escritorio\Proyecto algoritmos\interfaz\IMG.jpeg")  # Reemplaza "tu_imagen.jpg" con la ruta de tu propia imagen
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un widget Label para mostrar la imagen
etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
etiqueta_imagen.pack()

ventana.mainloop()