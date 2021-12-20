from modules import ROT

def input_int(msg: str):
    steps: int = 0
    try:
        steps = int(input(msg))
        if steps <= 0:
            print("Error, por favor ingrese un numero mayor a 0")
            steps = input_int(msg)
    except:
        print("Error, por favor ingrese un numero valido")
        steps = input_int(msg)
    return steps

def main():

    # Lee el mensaje a cifrar
    msg = input("\033[0;33m" + "Ingrese mensaje a cifrar: ")
    # Lee el numero de saltos
    steps = input_int("\033[0;33m" + "Ingrese el numero de saltos: ")

    # Encripta el mensaje como cadena de caracteres (por su posicion en el alfabeto)
    encripted: str = ROT.encrypt(msg, steps)
    # Desencripta el mensaje como cadena de caracteres (por su posicion en el alfabeto)
    decripted: str = ROT.decrypt(encripted, steps)
    # Imprime en pantalla el mensaje encriptado y desencriptado
    print("\033[1;36m" + "\nEncriptado por string" + "\033[0;37m")
    print("\033[0;31m" + encripted)
    print("\033[0;32m" + decripted)

    # Encripta el mensaje como bytes (por su posicion en la tabla ascii)
    bencripted: str = ROT.bencrypt(bytes(msg, "utf-8"), steps)
    # Desncripta el mensaje como bytes (por su posicion en la tabla ascii)
    bdecripted: str = ROT.bdecrypt(bencripted, steps)

    # Imprime en pantalla el mensaje encriptado y desencriptado
    print("\033[1;36m" + "\nEncriptado por bytes")
    print("\033[0;31m", end="")
    print(bencripted)
    print("\033[0;32m", end="")
    print(bdecripted)
    print("\033[0;37m", end="")
    return 0

if __name__ == "__main__":
    main()