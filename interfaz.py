import tkinter as tk
from tkinter import scrolledtext, PhotoImage
import subprocess

def ejecutar_analizador():
    consulta_sql = entrada_texto.get("1.0", tk.END).strip()
    
    if not consulta_sql:
        resultado_texto.insert(tk.END, "⚠ Por favor, ingresa una consulta SQL.\n")
        return
    
    try:
        resultado_texto.delete("1.0", tk.END)
        proceso = subprocess.run(
            ["C:/Users/ander/Documents/ADSOSA/Analizador SQL/New/AnalizadorSQL/analizador-sql.exe"],  # Asegúrate de colocar la ruta correcta
            input=consulta_sql,
            text=True,
            capture_output=True
        )
        resultado_texto.insert(tk.END, proceso.stdout)
    except Exception as e:
        resultado_texto.insert(tk.END, f"❌ Error al ejecutar: {e}\n")


ventana = tk.Tk()
ventana.title("🔍 Analizador Léxico SQL by Anderson Sosa")
ventana.geometry("700x700")
ventana.configure(bg="#1E1E2E") 

imagen_sql = PhotoImage(file="C:/Users/ander/Documents/ADSOSA/Analizador SQL/New/AnalizadorSQL/sql.png")  # Usa una imagen PNG de SQL
label_imagen = tk.Label(ventana, image=imagen_sql, bg="#1E1E2E")
label_imagen.pack(pady=10)

etiqueta = tk.Label(ventana, text="Ingrese la consulta SQL:", fg="white", bg="#1E1E2E", font=("Arial", 14))
etiqueta.pack()

entrada_texto = scrolledtext.ScrolledText(ventana, height=5, font=("Arial", 12))
entrada_texto.pack(padx=10, pady=5, fill="both", expand=True)


btn_ejecutar = tk.Button(ventana, text="🔍 Analizar", font=("Arial", 12, "bold"), bg="#3498db", fg="white", command=ejecutar_analizador)
btn_ejecutar.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Resultado:", fg="white", bg="#1E1E2E", font=("Arial", 14))
etiqueta_resultado.pack()
resultado_texto = scrolledtext.ScrolledText(ventana, height=10, font=("Courier", 12), bg="#282A36", fg="white")
resultado_texto.pack(padx=10, pady=5, fill="both", expand=True)

ventana.mainloop()
