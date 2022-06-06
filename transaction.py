import sqlite3

# Valores de prueba
uid = (0xAA, 0xBB, 0xCC, 0xDD) # tarjeta leida
uid_filtered = (int.from_bytes(uid, "big"),)
e_code = "1470" # codigo ingresado
price = 20000 # precio de transaccion ($200)

def verification_check(uid,code,price):
    uid_filtered = (int.from_bytes(uid, "big"),)
    print("uid_filtedes: "+ str(uid_filtered))
    # Abrir conexion al inicio
    con = sqlite3.connect("accounts.db")
    cur = con.cursor()

    # Buscar tarjeta en DB
    cur.execute("SELECT code, balance FROM accounts WHERE card_id=(?)", uid_filtered)


    # Obtener valores encontrados
    try:
        u_code, balance = cur.fetchone()
        #debug
        print(u_code + " " + balance)
    except TypeError:
        print("Tarjeta no encontrada")
        return False

    # Comparar codigo
    if e_code != u_code:
        print("Codigo incorrecto")
        return False

    # Checar balance
    if price > balance:
        print("Balance insuficiente")
        return False

    # Insertar nuevo valor
    new_balance = balance - price
    insertar = {"card_id": uid_filtered, "code": u_code, "balance": new_balance} 
    cur.execute("INSERT INTO accounts VALUES (:card_id, :code, :balance)", insertar)

    con.commit()
    con.close()
    return True