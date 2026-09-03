# =====================================================
# gestor.py — Programa principal del taller.
# TODO está resuelto acá: no hace falta tocar nada.
# Uso:  python gestor.py
# =====================================================

import json
import os

from contrasenas import (
    registrar_texto, verificar_texto,
    registrar_hash, verificar_hash,
    registrar_salt, verificar_salt,
)

ARCHIVO = "usuarios.json"

OPCIONES = {"1": "texto", "2": "hash", "3": "salt"}


def cargar():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, encoding="utf-8") as f:
            return json.load(f)
    return {}


def guardar(usuarios):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=2, ensure_ascii=False)


def elegir_metodo():
    print("\n¿Cómo se va a guardar la contraseña?")
    print("  1) Texto plano (¡inseguro! solo para comparar)")
    print("  2) Hash simple")
    print("  3) Hash con salt")
    eleccion = input("Elegí 1, 2 o 3: ").strip()
    return OPCIONES.get(eleccion, "texto")


def registrar(usuarios):
    usuario = input("Nombre de usuario: ").strip()
    if not usuario:
        return
    if usuario in usuarios:
        print("⚠ Ese usuario ya existe, probá con otro nombre.")
        return
    contrasena = input("Contraseña: ")
    metodo = elegir_metodo()

    if metodo == "texto":
        dato = registrar_texto(contrasena)
    elif metodo == "hash":
        dato = registrar_hash(contrasena)
    else:
        dato = registrar_salt(contrasena)

    usuarios[usuario] = {"metodo": metodo, "dato": dato}
    guardar(usuarios)
    print(f"\n✔ Usuario '{usuario}' guardado con método '{metodo}'.")


def iniciar_sesion(usuarios):
    usuario = input("Nombre de usuario: ").strip()
    if usuario not in usuarios:
        print("⚠ Usuario inexistente.")
        return
    contrasena = input("Contraseña: ")
    registro = usuarios[usuario]
    metodo = registro["metodo"]
    dato = registro["dato"]

    if metodo == "texto":
        ok = verificar_texto(dato, contrasena)
    elif metodo == "hash":
        ok = verificar_hash(dato, contrasena)
    else:
        ok = verificar_salt(dato, contrasena)

    if ok:
        print("✔ ¡Sesión iniciada!")
    else:
        print("✘ Contraseña incorrecta.")


def menu():
    print("=" * 50)
    print("  Taller de criptografía: gestor de contraseñas")
    print("  Consejo: con la opción 3 podés VER lo que queda")
    print("  guardado en el archivo. ¡Mirá con qué método!")
    print("=================================================")
    usuarios = cargar()
    while True:
        print("\n--- MENÚ ---")
        print("  1) Registrar usuario")
        print("  2) Iniciar sesión")
        print("  3) Ver usuarios.json (¡inspeccionar!)")
        print("  4) Salir")
        eleccion = input("> ").strip()
        if eleccion == "1":
            registrar(usuarios)
        elif eleccion == "2":
            iniciar_sesion(usuarios)
        elif eleccion == "3":
            print(json.dumps(usuarios, indent=2, ensure_ascii=False))
        elif eleccion == "4":
            print("¡Hasta la próxima!")
            break


if __name__ == "__main__":
    menu()