import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk
from tkinter import scrolledtext, PhotoImage, messagebox

# Tokens para SQL
tokens = (
    'SELECT', 'INSERT', 'UPDATE', 'DELETE', 'FROM', 'WHERE', 'INTO', 'VALUES', 'SET',
    'ID', 'NUMBER', 'COMMA', 'EQUALS', 'LPAREN', 'RPAREN', 'ASTERISK'
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_EQUALS = r'='
t_ASTERISK = r'\*'

def t_SELECT(t):
    r'SELECT'
    return t

def t_INSERT(t):
    r'INSERT'
    return t

def t_UPDATE(t):
    r'UPDATE'
    return t

def t_DELETE(t):
    r'DELETE'
    return t

def t_FROM(t):
    r'FROM'
    return t

def t_WHERE(t):
    r'WHERE'
    return t

def t_INTO(t):
    r'INTO'
    return t

def t_VALUES(t):
    r'VALUES'
    return t

def t_SET(t):
    r'SET'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Reglas de la gramática SQL
def p_statement_select(p):
    '''statement : SELECT column_list FROM ID
                 | SELECT column_list FROM ID WHERE ID EQUALS NUMBER'''
    p[0] = "Consulta SELECT válida"

def p_column_list(p):
    '''column_list : ASTERISK
                   | ID
                   | ID COMMA column_list'''
    pass

def p_statement_insert(p):
    '''statement : INSERT INTO ID LPAREN column_list RPAREN VALUES LPAREN value_list RPAREN'''
    p[0] = "Consulta INSERT válida"

def p_value_list(p):
    '''value_list : NUMBER
                  | NUMBER COMMA value_list'''
    pass

def p_statement_update(p):
    'statement : UPDATE ID SET ID EQUALS NUMBER WHERE ID EQUALS NUMBER'
    p[0] = "Consulta UPDATE válida"

def p_statement_delete(p):
    'statement : DELETE FROM ID WHERE ID EQUALS NUMBER'
    p[0] = "Consulta DELETE válida"

def p_error(p):
    if p:
        print(f"Error de sintaxis en la consulta SQL. Token inesperado: {p.value} en la línea {p.lineno}")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

parser = yacc.yacc()

def analizar_sql():
    entrada = entrada_texto.get("1.0", tk.END).strip()
    resultado_texto.delete("1.0", tk.END)
    resultado = parser.parse(entrada)
    resultado_texto.insert(tk.END, resultado if resultado else "Consulta SQL no válida")

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("🔍 Analizador Sintáctico SQL by Anderson Sosa")
ventana.geometry("700x700")
ventana.configure(bg="#1E1E2E")

imagen_sql = PhotoImage(file="C:/Users/User/Documents/Analizador sintactico/sql.png")
label_imagen = tk.Label(ventana, image=imagen_sql, bg="#1E1E2E")
label_imagen.pack(pady=10)

etiqueta = tk.Label(ventana, text="Ingrese la consulta SQL:", fg="white", bg="#1E1E2E", font=("Arial", 14))
etiqueta.pack()

entrada_texto = scrolledtext.ScrolledText(ventana, height=5, font=("Arial", 12))
entrada_texto.pack(padx=10, pady=5, fill="both", expand=True)

btn_ejecutar = tk.Button(ventana, text="🔍 Analizar", font=("Arial", 12, "bold"), bg="#3498db", fg="white", command=analizar_sql)
btn_ejecutar.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Resultado:", fg="white", bg="#1E1E2E", font=("Arial", 14))
etiqueta_resultado.pack()
resultado_texto = scrolledtext.ScrolledText(ventana, height=10, font=("Courier", 12), bg="#282A36", fg="white")
resultado_texto.pack(padx=10, pady=5, fill="both", expand=True)

ventana.mainloop()