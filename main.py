import tkinter as tk
import json
import os


def Add():
  win1.withdraw()
  win2 = tk.Tk()
  win2.title("Add info")
  win2.geometry("620x620")
  
  labelst = tk.Label(win2, text="Type the web/source:")
  labelst.pack()
  Web = tk.Text(win2, width=20, height=1)
  Web.pack()
  labelus = tk.Label(win2, text="Type the user:")
  labelus.pack()
  user = tk.Text(win2,width=20 , height=1)
  user.pack()
  labelpas = tk.Label(win2, text="Type the password:")
  labelpas.pack()
  Password = tk.Text(win2, width=20, height=1)
  Password.pack()

  def save_data():
    where = Web.get("1.0", tk.END).strip()
    userfin = user.get("1.0", tk.END).strip()
    passfin = Password.get("1.0",tk.END).strip()
    if not os.path.exists("datos.json") or os.path.getsize("datos.json") == 0:
        contenido_json = []
    else:
        with open("datos.json", "r") as a:
            contenido_json = json.load(a)

    data = {
        "enterprise": where,
        "userfin": userfin,
        "passfin": passfin
    }
    
    contenido_json.append(data)
    with open("datos.json", "w") as b:
      json.dump(contenido_json, b)
      
    Web.delete("1.0", tk.END)
    user.delete("1.0", tk.END)
    Password.delete("1.0", tk.END)
    
  guardar = tk.Button(win2, text = "Save", command=save_data)
  guardar.pack()
  


def Search():
  win1.withdraw()
  winsearch = tk.Tk()
  winsearch.title("Search info")
  winsearch.geometry("720x720")
  labelstb = tk.Label(winsearch, text="Type the web/source:")
  labelstb.pack()
  source =tk.Text(winsearch, width=20, height = 1)
  source.pack()

  def search_data():
      if not os.path.exists("datos.json") or os.path.getsize("datos.json") == 0:
        contenido_json = []

      else:

        with open("datos.json", "r") as a:
            contenido_json = json.load(a)
          
      search_term = source.get("1.0", tk.END).strip()
      busqueda_encontrada = None
    
      for data in contenido_json:
        if data["enterprise"] == search_term:
          tofind_term = data
          break
          
      havefind_text_text = tk.Text(winsearch, width=80, height=40)
      
          
          
      if tofind_term:
        havefind_text = f"This is what has been found with the searched term: {search_term}\n"
        havefind_text += f"Account: {data['userfin']}\n"
        havefind_text += f"Password: {data['passfin']}\n"
      else:
        havefind_text = "No fue encontrado"
      
      havefind_text_text.pack()
      havefind_text_text.insert("1.0", havefind_text)  
          
  searchbutton = tk.Button(winsearch, text = "Search", command=search_data)
  searchbutton.pack()

# Crear una ventana
win1 = tk.Tk()

# Configurar propiedades de la ventana
win1.title("Index. PassKeeper 1.0")
win1.geometry("620x620")

# Crear un widget de etiqueta
label1 = tk.Label(win1, text="Select the option that suits you.")
label1.pack()

# Crear un widget de botón
A = tk.Button(win1, text="Add", command=Add)
A.pack()
B = tk.Button(win1, text="Search", command=Search)
B.pack()
C =tk.Label(win1, text="BETA: limited capabilities")
# Ejecutar el bucle principal de la aplicación
win1.mainloop()
