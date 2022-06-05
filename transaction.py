import sqlite3

# Valores de prueba
uid = (0xAA, 0xBB, 0xCC, 0xDD) # tarjeta leida
e_code = "1470" # codigo ingresado
price = 200_00 # precio de transaccion ($200)

# Abrir conexion al inicio
con = sqlite3.connect("accounts.db")
cur = con.cursor()

# Buscar tarjeta en DB
cur.execute("SELECT code, balance FROM accounts WHERE card_id=(?)", (int.from_bytes(uid, "big"),))

# Obtener valores encontrados
try:
    u_code, balance = cur.fetchone()
except TypeError:
    print("Tarjeta no encontrada")
    exit()

# Comparar codigo
if e_code != u_code:
    print("Codigo incorrecto")
    exit()

# Checar balance
if price > balance:
    print("Balance insuficiente")
    exit()

