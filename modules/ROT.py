# Listas para el encriptado por cadena de caracteres
__alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
__upperAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
__numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Agrega los saltos al mensaje
def __add_steps(value: int, limit: int, steps: int):
    add : int = value + steps
    add %= limit
    if add >= limit:
        add - limit
    return add

# Resta los saltos al mensaje
def __substract_steps(value: int, limit: int, steps: int):
    sub: int = value - steps
    sub %= limit
    if sub < 0:
        sub + limit
    return sub

# Realiza el encriptado para cada letra y lo une en una sola cadena de caracteres
def encrypt(msg: str, steps: int):
    enc: str = ""
    for ch in msg:
        if ch in __alphabet:
            enc = enc + __alphabet[__add_steps(__alphabet.index(ch), len(__alphabet), steps)]
        elif ch in __upperAlphabet:
            enc = enc + __upperAlphabet[__add_steps(__upperAlphabet.index(ch), len(__upperAlphabet), steps)]
        elif ch in __numbers:
            enc = enc + __numbers[__add_steps(__numbers.index(ch), len(__numbers), steps)]
        else:
            enc = enc + ch
    return enc

# Realiza el desencriptado para cada letra y lo une en una sola cadena de caracteres
def decrypt(enc: str, steps: int):
    msg: str = ""
    for ch in enc:
        if ch in __alphabet:
            msg = msg + __alphabet[__substract_steps(__alphabet.index(ch), len(__alphabet), steps)]
        elif ch in __upperAlphabet:
            msg = msg + __upperAlphabet[__substract_steps(__upperAlphabet.index(ch), len(__upperAlphabet), steps)]
        elif ch in __numbers:
            msg = msg + __numbers[__substract_steps(__numbers.index(ch), len(__numbers), steps)]
        else:
            msg = msg + ch
    return msg
    
# Realiza el encriptado para cada letra y lo une en un solo arreglo de bytes
def bencrypt(msg: bytes, steps: int):
    enc: bytes = b""
    for ch in msg:
        enc = b"".join([enc, int(__add_steps(ch, 256, steps)).to_bytes(1, "big")])
    return enc

# Realiza el desencriptado para cada letra y lo une en un solo arreglo de bytes
def bdecrypt(enc: bytes, steps: int):
    msg: bytes = b""
    for ch in enc:
        msg = b"".join([msg, int(__substract_steps(ch, 256, steps)).to_bytes(1, "big")])
    return msg