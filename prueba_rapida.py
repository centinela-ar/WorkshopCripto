# Corre esto después de completar cada paso:
#   python prueba_rapida.py
import time
from contrasenas import registrar_hash, verificar_hash, registrar_salt, verificar_salt

PASS_TEST = "hola"
OK = "  [OK]"
MAL = "  [FALLO]"


def test(nombre, condicion):
    print(f"{nombre}: {OK if condicion else MAL}" if False else f"{nombre}: {'[OK]' if condicion else '[FALLO]'}")


print("--- Probando PASO 1 (hash simple) ---")
esperado_hola = "b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79"  # SHA-256 de "hola"
test("PASO 1a: hash de 'hola' es el esperado", registrar_hash("hola") == esperado_hola)
h = registrar_hash("hola")
print(f"PASO 1a  hash('hola'):  {'[OK]' if h == esperado_hola else '[FALLO]'}")
v = verificar_hash(h, PASS_TEST) if h is not None else False
print(f"PASO 1b  verificar:     {'[OK]' if v else '[FALLO]'}")

print("--- Probando PASO 2 (hash con salt) ---")
try:
    dato = registrar_salt(PASS_TEST)
    ok_reg = isinstance(dato, dict) and "salt" in dato and "hash" in dato
    print(f"PASO 2a  registro:      {'[OK]' if ok_reg else '[FALLO]'}")
    ok_ver = ok_reg and verificar_salt(dato, PASS_TEST) is True
    ok_falso = ok_reg and verificar_salt(dato, "otra-clave") is False
    print(f"PASO 2b  verificar:     {'[OK]' if ok_ver else '[FALLO]'}")
    print(f"PASO 2c  rechaza malas: {'[OK]' if ok_falso else '[FALLO]'}")
    if ok_reg:
        dato2 = registrar_salt(PASS_TEST)
        distinto = dato["hash"] != dato2["hash"]
        print(f"BONUS    misma pass -> hashes distintos: {'[OK]' if distinto else '[FALLO]'}")
except Exception as e:
    print(f"PASO 2   ERROR: {e}")
