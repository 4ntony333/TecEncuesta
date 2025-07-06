from tkinter import Tk, Label, Entry, Button, Text, StringVar, OptionMenu, END

costos = {
    "tablet": 600,
    "laptop": 1200,
    "internet": 300,
    "capacitacion": 150
}

personas = []

def agregar_persona():
    persona = {
        "nombre": nombre_var.get(),
        "edad": int(edad_var.get()),
        "internet": internet_var.get(),
        "dispositivo": dispositivo_var.get(),
        "uso": uso_var.get()
    }
    personas.append(persona)
    salida_text.insert(END, f"Agregado: {persona['nombre']} ({persona['edad']} años)\n")

def asignar_recursos():
    salida_text.insert(END, "\n=== RESULTADOS ===\n")
    for p in personas:
        recursos = []
        presupuesto = 0

        if p["internet"] == "No tiene":
            recursos.append("Internet")
            presupuesto += costos["internet"]

        if p["dispositivo"] == "Ninguno":
            recursos.append("Tablet")
            presupuesto += costos["tablet"]

        if p["uso"] in ["nulo", "limitado"]:
            recursos.append("Capacitación")
            presupuesto += costos["capacitacion"]

        salida_text.insert(END, f"{p['nombre']} ({p['edad']} años): {', '.join(recursos) if recursos else 'Ninguno'} - S/. {presupuesto}\n")

app = Tk()
app.title("Asignación de Recursos Tecnológicos")

nombre_var = StringVar()
edad_var = StringVar()
internet_var = StringVar(value="Internet en casa")
dispositivo_var = StringVar(value="Laptop")
uso_var = StringVar(value="educación")

Label(app, text="Nombre:").grid(row=0, column=0)
Entry(app, textvariable=nombre_var).grid(row=0, column=1)

Label(app, text="Edad:").grid(row=1, column=0)
Entry(app, textvariable=edad_var).grid(row=1, column=1)

Label(app, text="Internet:").grid(row=2, column=0)
OptionMenu(app, internet_var, "Internet en casa", "Datos móviles", "No tiene").grid(row=2, column=1)

Label(app, text="Dispositivo:").grid(row=3, column=0)
OptionMenu(app, dispositivo_var, "Laptop", "Celular", "Tablet", "Ninguno").grid(row=3, column=1)

Label(app, text="Uso:").grid(row=4, column=0)
OptionMenu(app, uso_var, "educación", "entretenimiento", "nulo", "limitado").grid(row=4, column=1)

Button(app, text="Agregar Persona", command=agregar_persona).grid(row=5, column=0, columnspan=2)
Button(app, text="Asignar Recursos", command=asignar_recursos).grid(row=6, column=0, columnspan=2)

salida_text = Text(app, height=10, width=50)
salida_text.grid(row=7, column=0, columnspan=2)

app.mainloop()

