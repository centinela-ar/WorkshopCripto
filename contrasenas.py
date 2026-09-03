# =====================================================
# contrasenas.py — AQUÍ TRABAJAN USTEDES
#
# Hay 3 pasos. Haganlos EN ORDEN y corran:
# python prueba_rapida.py
# después de cada uno para verificar.
# =====================================================

import hashlib
import secrets

# ---------------------------------------------------------------
# PASO 0 (ya resuelto, úsenlo de ejemplo)
# Guardar la contraseña tal cual. Esto es lo que hacen los
# programas MAL HECHOS. Lo dejamos para poder comparar después.
# ---------------------------------------------------------------
def registrar_texto(contrasena):
    return contrasena


def verificar_texto(dato_guardado, contrasena_ingresada):
    return dato_guardado == contrasena_ingresada


# ---------------------------------------------------------------
# PASO 1: guardar un HASH simple (sin salt)
# ---------------------------------------------------------------
def registrar_hash(contrasena):
    """
    Debe devolver el hash SHA-256 de la contraseña, como texto.

    Pistas:
      - hashlib.sha256(...) calcula el hash, pero necesita BYTES,
        no texto: pásenle contrasena.encode("utf-8")
      - Agreguen .hexdigest() al final para obtener texto legible.
    Ejemplo: "hola" ->
      'b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79'
    """
    # BODY (1 línea): reemplacen 'pass' por el return correspondiente
    pass


def verificar_hash(dato_guardado, contrasena_ingresada):
    """
    Debe devolver True si el hash de la contraseña ingresada
    coincide con el hash guardado.
    """
    # BODY (1 línea)
    pass


# ---------------------------------------------------------------
# PASO 2: guardar un HASH CON SALT
# ---------------------------------------------------------------
def registrar_salt(contrasena):
    """
    La generación del salt YA ESTÁ hecha:
      salt = secrets.token_hex(16)  ->  32 caracteres al azar

    Les queda:
      - Calcular el hash de (salt + contrasena).encode("utf-8")
      - Devolver un diccionario: {"salt": salt, "hash": el_hash}
    """
    salt = secrets.token_hex(16)
    hash_con_salt = hashlib.sha256((salt + contrasena).encode("utf-8")).hexdigest()
    return {"salt": salt, "hash": hash_con_salt}

    # BODY (2 líneas): calcular el hash y hacer el return
    pass


def verificar_salt(dato_guardado, contrasena_ingresada):
    """
    dato_guardado es un diccionario con las claves "salt" y "hash".
    Pista: para tomar el salt usan dato_guardado["salt"] o la clave que le hayan puesto en el registrar_salt.

    Debe devolver True si la contraseña ingresada es la correcta.
    """
    # BODY (2 líneas)
    pass