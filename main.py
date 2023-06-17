import tkinter as tk
import json
import os

# Definimos que hacer al pulsar el botón de Añadir
def Add():
  ventanauno.withdraw()
  ventanados = tk.Tk()
  ventanados.title("Add info")
  ventanados.geometry("620x620")
    # Función para guardar los datos en un archivo JSON
  labelst = tk.Label(ventanados, text="Página web de donde procede")
  labelst.pack()
  Web = tk.Text(ventanados, width=20, height=1)
  Web.pack()
  labelus = tk.Label(ventanados, text="Escriba su usuario/correo")
  labelus.pack()
  Usuario = tk.Text(ventanados,width=20 , height=1)
  Usuario.pack()
  labelpas = tk.Label(ventanados, text="Escriba su contraseña/credencial")
  labelpas.pack()
  Password = tk.Text(ventanados, width=20, height=1)
  Password.pack()

  #Definimos como guardar datos
  def guardar_datos():
    where = Web.get("1.0", tk.END).strip()
    usuariofin = Usuario.get("1.0", tk.END).strip()
    passfin = Password.get("1.0",tk.END).strip()
    if not os.path.exists("datos.json") or os.path.getsize("datos.json") == 0:
        # El archivo no existe o está vacío, crear una lista vacía
        contenido_json = []
    else:
        with open("datos.json", "r") as a:
            contenido_json = json.load(a)

    datos = {
        "enterprise": where,
        "usuariofin": usuariofin,
        "passfin": passfin
    }
    
    contenido_json.append(datos)
    with open("datos.json", "w") as b:
      json.dump(contenido_json, b)
      
    Web.delete("1.0", tk.END)
    Usuario.delete("1.0", tk.END)
    Password.delete("1.0", tk.END)
    
  guardar = tk.Button(ventanados, text = "Save", command=guardar_datos)
  guardar.pack()

#Definimos que queremos que ocurra al pulsar el botón de Buscar

def Search():
  ventanauno.withdraw()
  ventanasearch = tk.Tk()
  ventanasearch.title("Search info")
  ventanasearch.geometry("720x720")
  labelstb = tk.Label(ventanasearch, text="Escriba aquí el dominio de la web")
  labelstb.pack()
  empresa =tk.Text(ventanasearch, width=20, height = 1)
  empresa.pack()

  def buscar_datos():
      if not os.path.exists("datos.json") or os.path.getsize("datos.json") == 0:
        # El archivo no existe o está vacío, crear una lista vacía
        contenido_json = []
      else:
        with open("datos.json", "r") as a:
            contenido_json = json.load(a)
          
      busqueda = empresa.get("1.0", tk.END).strip()
      busqueda_encontrada = None
    
      for datos in contenido_json:
        if datos["enterprise"] == busqueda:
          busqueda_encontrada = datos
          break
          
      busqueda_encontrada_text = tk.Text(ventanasearch, width=80, height=40)
      busqueda_encontrada_text.pack()
          
          
      if busqueda_encontrada:
        texto_encontrar = f"Esto es lo que se ha encontrado con el término buscado: {busqueda}\n"
        texto_encontrar += f"Cuenta: {datos['usuariofin']}\n"
        texto_encontrar += f"Contraseña: {datos['passfin']}\n"
      else:
        texto_encontrar = "No fue encontrado"
          
      busqueda_encontrada_text.insert("1.0", texto_encontrar)  
          
  buscar = tk.Button(ventanasearch, text = "Search", command=buscar_datos)
  buscar.pack()

# Crear una ventana
ventanauno = tk.Tk()

# Configurar propiedades de la ventana
ventanauno.title("Index. PassKeeper 1.0")
ventanauno.geometry("620x620")

# Crear un widget de etiqueta
label1 = tk.Label(ventanauno, text="Seleccione la opción que le convenga.")
label1.pack()

# Crear un widget de botón
A = tk.Button(ventanauno, text="Añade", command=Add)
A.pack()
B = tk.Button(ventanauno, text="Buscar", command=Search)
B.pack()
# Ejecutar el bucle principal de la aplicación
ventanauno.mainloop()
