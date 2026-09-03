# 🔐 Taller de Criptografía — Día 1: Contraseñas, Hashes y Salt

Bienvenido/a. En esta práctica vamos a construir, un pequeño gestor de contraseñas que guarda las contraseñas de **tres formas distintas**, para ver con tus ojos cuáles son seguras y cuáles no.

## 🎯 Lo que vas a aprender

Al terminar esta práctica vas a poder responder:

1. ¿Por qué **nunca** se guarda una contraseña en texto plano?
2. ¿Qué es un **hash** y por qué es "de una sola vía"?
3. ¿Qué es una **tabla arcoiris** y qué riesgos supone?
4. ¿Qué problema resuelve el **salt**? ¿Por qué dos personas con la misma
   contraseña terminan con datos guardados completamente diferentes?

## ✅ Requisitos

- Tener instalado **Python 3** (probalo abriendo una terminal y escribiendo `python --version`
  o `python3 --version`).
- **Nada más.** No se instala ninguna librería: todo lo que usamos viene incluido en Python.

## 📁 Archivos del proyecto

| Archivo            | ¿Qué es?                                                     |
| ------------------ | ------------------------------------------------------------ |
| `gestor.py`        | El programa principal. **Ya está completo, no lo toques.**   |
| `contrasenas.py`   | ⭐ **El único archivo que vas a editar.** Contiene los 3 pasos. |
| `prueba_rapida.py` | Tu corrector automático. Te dice si cada paso quedó bien.    |
| `romper_hash.py`   | Bonus: un "atacante" que intenta adivinar contraseñas.       |
| `diccionario.txt`  | Lista de contraseñas comunes que usa el atacante.            |
| `usuarios.json`    | Se crea solo cuando registrás usuarios. ¡Miralo!             |

## 🚀 Cómo empezar

1. Descargá el proyecto (botón verde **Code → Download ZIP**, o:

   ```bash
   git clone <URL-del-repositorio>
   cd gestor
   ```

2. Abrí `contrasenas.py` en tu editor (VS Code, Bloc de notas, vim, el que quieras o tengas).

3. Dejá abierta una terminal parada en la carpeta del proyecto.

> 💡 **Consejo:** trabajen en grupos de a dos o de a tres. Mientras uno escribe, otro revisa, pueden invertir roles durante el taller.

## 🪜 Los pasos (¡en orden!)

### PASO 0 — Ya está hecho (para comparar)

La función `registrar_texto()` guarda la contraseña **tal cual**. Así hacen los programas malos, sorprendentemente aún se encuentran varios en producción. No hay que tocar nada: solo registrá un usuario con el método
"1) Texto plano" desde `gestor.py` y mirá `usuarios.json` (opción 3 del menú).
Vas a ver tu contraseña, en claro, tal cual la escribiste. 😱

Corré el programa:

```bash
python gestor.py
```

### PASO 1 — Hash simple

En `contrasenas.py`, completá `registrar_hash()` y `verificar_hash()`.
Las pistas están en los comentarios del archivo.

Cuando termines, verificá:

```bash
python prueba_rapida.py
```

Si ves `[OK]` en el PASO 1, podés registrar un usuario con el método 2) Hash simple y volver a mirar `usuarios.json`. Tu contraseña ya no aparece... ¡veremos qué ocurre en la Demo!

### PASO 2 — Hash con salt

Completá `registrar_salt()` y `verificar_salt()`.
El código del salt ya está bastante avanzado.

Verificá otra vez:

```bash
python prueba_rapida.py
```

Después registrá un usuario con el método "3) Hash con salt", mirá `usuarios.json` y notá una cosa clave: **registrá al mismo usuario con la misma contraseña dos veces → el hash guardado es distinto cada vez.**
¡Eso es el salt trabajando!

### 🏆 BONUS — El ataque (para parejas que terminaron)

Uno de la pareja registra una contraseña con hash simple, copia el hash de `usuarios.json` y se lo pasa al otro. El otro intenta "romperlo":

```bash
python romper_hash.py
```

Pegá el hash cuando lo pida. ¿La adivinó? ¿En cuánto tiempo?
Ahora inténtenlo con una contraseña que **no** esté en `diccionario.txt`, y luego con el modo "hash con salt" (van a descubrir que el ataque ya no funciona tan fácil, aunque tengan la contraseña... ¿por qué? 😉).

## 🧪 Tu corrector automático

`prueba_rapida.py` verifica cada paso apenas lo completes:

```
--- Probando PASO 1 (hash simple) ---
PASO 1a  hash('hola'):  [OK]
PASO 1b  verificar:     [OK]

--- Probando PASO 2 (hash con salt) ---
PASO 2a  registro:      [OK]
...
```

Correlo **después de cada paso**. Si algo falla, no avances: revisá las pistas del comentario arriba del TODO.

## 🆘 Problemas comunes

| Mensaje                                            | Qué significa                                                |
| -------------------------------------------------- | ------------------------------------------------------------ |
| `NameError: hashlib is not defined`                | No corras el archivo directamente sin los imports — usá la plantilla que ya viene con los `import` al inicio. |
| `TypeError: can only concatenate str...`           | En el PASO 2 estás mezclando texto con bytes. Todo lo que entra al hash debe estar `.encode("utf-8")`. |
| `SyntaxError` al correr                            | Seguramente borraste un paréntesis o los dos puntos. Revisá la línea que acabás de editar. |
| La prueba da `[FALLO]` pero el programa "funciona" | Fijate que el `return` devuelva lo pedido: en el PASO 1 un string con `.hexdigest()`, en el PASO 2 un diccionario con `"salt"` y `"hash"`. |

Si te trabás más de 10 minutos: **¡Avisá!**. No es rendir, es parte del juego y del aprendizaje.

## 🌍 Y en el mundo real, ¿qué se usa?

Un detalle final para cerrar la historia completa:

Los hashes que usamos hoy (**SHA-256**) fueron diseñados para ser **rápidos**. Eso es perfecto para verificar archivos, pero **terrible para contraseñas**: un atacante puede probar miles de millones de contraseñas por segundo.

Por eso, en sistemas reales, no se recomienda tanto SHA-256 directo, sino funciones **diseñadas para ser lentas a propósito** y que además traen el salt incluido:

- **PBKDF2** (incluida en Python: `hashlib.pbkdf2_hmac`)
- **bcrypt** y **argon2** (los estándares actuales)

Si algo de esto te interesó, tenés material para profundizar toda la carrera. 😄



## ⚖️ Uso exclusivamente educativo

Este proyecto fue creado para un taller introductorio de criptografía. Los programas que contiene son simplificaciones didácticas: **no deben usarse para proteger sistemas reales** ni como base de software en producción. El script `romper_hash.py` incluye un ataque de diccionario con fines demostrativos, para que vean cómo un atacante explota contraseñas débiles y por qué las buenas prácticas importan. Usarlo contra sistemas, cuentas o servicios de terceros es ilegal y contrario al espíritu del taller. Si querés aplicar lo aprendido, hacelo sobre tus propias contraseñas de prueba, en tu propia máquina.

## 📄 Licencia

Este material se distribuye bajo la licencia [MIT] (./LICENSE). Podés usarlo, modificarlo y compartirlo libremente, incluyendo el uso en clase, citando la fuente.
