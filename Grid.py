import tkinter as tk

def registrar():
    global frame
    nombre = cnombre.get()
    apellido = capellido.get()
    edad = cedad.get()
    sexo = "Masculino" if seleccion.get() == 1 else "Femenino"
    ciudad = ciudades.get()
    telefono = ctelefono.get()
    direccion = cdireccion.get()

    lframeinfo.config(text=f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nSexo: {sexo}\nCiudad: {ciudad}\nTeléfono: {telefono}\nDirección: {direccion}")

ventana = tk.Tk()
ventana.title("tecnar app")
ventana.geometry("800x600")
ventana.resizable(True, True)

lnombre = tk.Label(ventana, text="Nombre:")
lnombre.grid(row=0, column=0, padx=10, pady=10)
cnombre = tk.Entry(ventana, width=30)
cnombre.grid(row=0, column=1, padx=10, pady=10)

lapellido = tk.Label(ventana, text="Apellido:")
lapellido.grid(row=1, column=0, padx=10, pady=10)
capellido = tk.Entry(ventana, width=30)
capellido.grid(row=1, column=1, padx=10, pady=10)

ledad = tk.Label(ventana, text="Edad:")
ledad.grid(row=2, column=0, padx=10, pady=10)
cedad = tk.Entry(ventana, width=30)
cedad.grid(row=2, column=1, padx=10, pady=10)

ltelf = tk.Label(ventana, text="Teléfono:")
ltelf.grid(row=4, column=0, padx=10, pady=10)
ctelefono = tk.Entry(ventana, width=30)
ctelefono.grid(row=4, column=1, padx=10, pady=10)

ldireccion = tk.Label(ventana, text="Dirección:")
ldireccion.grid(row=5, column=0, padx=10, pady=10)
cdireccion = tk.Entry(ventana, width=30)
cdireccion.grid(row=5, column=1, padx=10, pady=10)

seleccion = tk.IntVar()
lsexo = tk.Label(ventana, text="Sexo:")
lsexo.grid(row=3, column=0, padx=10, pady=10)
masculino = tk.Radiobutton(ventana, text="Masculino", variable=seleccion, value=1)
masculino.grid(row=3, column=1, padx=10, pady=10)
femenino = tk.Radiobutton(ventana, text="Femenino", variable=seleccion, value=2)
femenino.grid(row=3, column=2, padx=10, pady=10)

ciudades_colombia = [
    "Armenia",
    "Barranquilla",
    "Bogota",
    "Bucaramanga",
    "Cali",
    "Cartagena",
    "Cucuta",
    "Ibague",
    "Manizales",
    "Medellin"
]

ciudades = tk.StringVar(ventana)
ciudades.set(ciudades_colombia[0])

lciudad = tk.Label(ventana, text="Ciudad:")
lciudad.grid(row=6, column=0, padx=10, pady=10)
menu_ciudades = tk.OptionMenu(ventana, ciudades, *ciudades_colombia)
menu_ciudades.grid(row=6, column=1, padx=10, pady=10)

bregistrar = tk.Button(ventana, text="Registrar", command=registrar)
bregistrar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

frame = tk.Frame(ventana, width=200, height=150, relief="raised", bd=1)
frame.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

lframeinfo = tk.Label(frame)
lframeinfo.grid(row=0, column=0)

ventana.mainloop()