import tkinter as tk

def pritisni_gumb(vrednost):
    trenutni_vnos = izraz.get()
    izraz.set(trenutni_vnos + str(vrednost))

def izracunaj():
    try:
        rezultat = eval(izraz.get())
        izraz.set(rezultat)
    except Exception as e:
        izraz.set("Napaka")

def pobrisi_vse():
    izraz.set("")

# Ustvarjanje glavnega okna
okno = tk.Tk()
okno.title("Grafični Kalkulator")

# Spremenljivka za shranjevanje izraza
izraz = tk.StringVar()

# Polje za prikaz izraza
polje_izraza = tk.Entry(okno, textvariable=izraz, font=("Arial", 14), justify="right", bd=10)
polje_izraza.grid(row=0, column=0, columnspan=4)

# Gumbi za števila
gumbi_stevila = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 1)
]

for (stevilo, vrstica, stolpec) in gumbi_stevila:
    gumb = tk.Button(okno, text=stevilo, padx=20, pady=20, font=("Arial", 14), command=lambda v=stevilo: pritisni_gumb(v))
    gumb.grid(row=vrstica, column=stolpec)

# Gumbi za operacije
gumbi_operacije = [
    ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3),
    ("=", 4, 2), ("C", 4, 0)
]

for (operacija, vrstica, stolpec) in gumbi_operacije:
    gumb = tk.Button(okno, text=operacija, padx=20, pady=20, font=("Arial", 14), command=lambda v=operacija: pritisni_gumb(v) if v != "=" else izracunaj())
    gumb.grid(row=vrstica, column=stolpec)

# Glavna zanka programa
okno.mainloop()
