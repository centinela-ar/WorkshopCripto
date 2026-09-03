# BONUS: intenten adivinar la contraseña original a partir del hash.
# USO EXCLUSIVAMENTE EDUCATIVO: probalo solo sobre hashes propios de este
# taller. Nunca contra cuentas o sistemas de terceros.
# Uso:  python romper_hash.py
# Peguen el hash que aparece al registrarse (modo "hash simple").

import time

with open("diccionario.txt", encoding="utf-8") as f:
    diccionario = [linea.strip() for linea in f if linea.strip()]

objetivo = input("Pegá el hash a romper: ").strip()
inicio = time.time()
encontrada = None
for palabra in diccionario:
    hash_calculado = __import__("hashlib").sha256(palabra.encode("utf-8")).hexdigest()
    if hash_calculado == objetivo:
        encontrada = palabra
        break

if encontrada:
    print(f"¡HASH ENCONTRADO! La contraseña era: {encontrada}")
else:
    print("No está en el diccionario.")
print(f"Probé {len(diccionario)} palabras en {time.time() - inicio:.2f} segundos.")