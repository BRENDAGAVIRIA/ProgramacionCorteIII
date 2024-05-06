import tkinter as tk
from PIL import Image, ImageTk 

def iniciar_sesion():
    print("Iniciando sesión...")

ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("800x500")
ventana.configure(bg="white")


frame_izquierdo = tk.Frame(ventana, bg="white", width=400, height=400, padx=30)
frame_izquierdo.place(relx=0.1, rely=0.5, anchor="w")


logo = Image.open("C:\\Users\\Usuario\\OneDrive\\Escritorio\\brenda.py\\logo_name.jpg")
logo = logo.resize((300,300))
logo = ImageTk.PhotoImage(logo)
label = tk.Label(image=logo,background="medium orchid")
label.place(x=60,y=100)



frame_derecho = tk.Frame(ventana, bg="white", width=200, height=400, padx=10)
frame_derecho.place(relx=0.7, rely=0.5, anchor="center")

titulo_label = tk.Label(frame_derecho, text="Inicio de Sesión", font=("bahnschrift", 18), bg="purple", fg="white")
titulo_label.pack(pady=20)

usuario_label = tk.Label(frame_derecho, text="Usuario:", font=("Helvetica", 12))
usuario_label.pack()

usuario_entry = tk.Entry(frame_derecho, font=("Helvetica", 12))
usuario_entry.pack(pady=5)

clave_label = tk.Label(frame_derecho, text="Clave:", font=("bahnschrift", 12))
clave_label.pack()

clave_entry = tk.Entry(frame_derecho, show="*", font=("bahnschrift", 12))
clave_entry.pack(pady=5)

ingresar_button = tk.Button(frame_derecho, text="Ingresar", command=iniciar_sesion, font=("bahnschrift", 12), bg="purple", fg="white")
ingresar_button.pack(pady=20, fill="x")

ventana.mainloop()