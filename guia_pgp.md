# 🔐 Guion del Alumno - Opcional: PGP entre pares

## 🎯 Qué vas a hacer?

1. Crear **tu propio par de claves** (privada + pública).
2. Intercambiar tu clave pública con tu pareja.
3. Cifrarle un archivo secreto y descifrar el que te envíe.
4. Firmar un documento y verificar la firma de tu pareja.

Es exactamente lo que hace TLS entre máquinas, pero entre **personas**:
vos sos tu propia autoridad.

## ✅ Antes de empezar

Necesitás **GnuPG** (`gpg`) instalado:

- **Linux:** ya viene instalado. Probalo: `gpg --version`
- **Windows:** instalá [Gpg4win](https://www.gpg4win.org/) (incluye Kleopatra)
- **Mac:** instalá [GPG Suite](https://gpgtools.org)

> ⚠️ **Las claves de esta práctica son de práctica.** No uses el email
> que escribas acá para nada real: esta clave debería borrarse al
> terminar la clase.

## 📝 Paso 0 — Anotá tus datos

Antes de crear la clave, decidí con tu pareja qué van a anotar (la
identificación se hace con email, así que acuérdense bien):

- **Mi nombre** para la clave: ______________________
- **Mi email de práctica**: (ej: `ana.mesa3@aula.edu`)
- El **email de mi pareja** (para cifrarle): ____________

## 🔑 Paso 1 — Creá tu par de claves (~5 min)

```bash
gpg --full-generate-key
```

Respondé así a las preguntas:

| Pregunta | Contestá |
|---|---|
| Tipo de clave | `1` (RSA y RSA) |
| Tamaño | 3072 |
| Validez | `0` (no expira) |
| ¿Realname? | Tu nombre |
| Email | El que anotaste arriba |
| Comentario | Enter (vacío) |
| Todo correcto | `O` (Ok) |
| Passphrase | Una frase corta, **anotala**: te la va a pedir varias veces |

Verificá que quedó creada:

```bash
gpg --list-keys
```

✔ **Deberías ver una clave con tu nombre y email.**

## 🤝 Paso 2 — Intercambien las claves públicas

Cada uno exporta su pública:

```bash
gpg --export -a "Mi Nombre" > mi_clave_publica.asc
```

Pasenle el archivo `mi_clave_publica.asc` a tu pareja (por correo,
pendrive o carpeta compartida), e importá **la de tu pareja**:

```bash
gpg --import clave_de_mi_pareja.asc
gpg --list-keys
```

✔ **Ahora tu llavero muestra DOS claves: la tuya y la de tu pareja.**

⚠ **Cuidado:** solo les van a pasar `clave_publica.asc`. La clave
**privada** jamás sale de tu computadora.

## Paso 3 — Cifrale un mensaje secreto a tu pareja

Creá un mensaje:

```bash
echo "El secreto del taller: nos vemos la proxima ALE" > mensaje_secreto.txt
```

Cifralo **con la clave de tu pareja** (el destinatario):

```bash
gpg --encrypt -a -r "email-de-mi-pareja" mensaje_secreto.txt
```

Fijate qué se generó: `mensaje_secreto.txt.asc` — abrilo y miralo.
Es ilegible. Eso es lo que ve un atacante. 😎

```bash
cat mensaje_secreto.txt.asc
```

Pasáselo a tu pareja. Lo descifra con **su clave privada**:

```bash
gpg --decrypt mensaje_secreto.txt.asc > mensaje_leido.txt
cat mensaje_leido.txt
```

🔒 **Testeo importante (hacelo):** intentá descifrar vos el mensaje que
vos mismo cifraste:

```bash
gpg --decrypt mensaje_secreto.txt.asc
```

**Va a fallar.** Cifrate con la clave pública de OTRO; solo el dueño
de esa clave privada puede leer. No importa que el mensaje lo hayas
escrito vos: quien cifra no puede descifrar. Si tu pareja puede leerlo
y vos no, el sistema funciona exactamente como debe. 😉

## ✍️ Paso 4 — Firma digital

Creamos un anuncio y lo firmamos con nuestra clave **privada**
(prueba de autoría):

```bash
echo "El parcial es el 15/09" > anuncio.txt
gpg --clearsign anuncio.txt
```

Tu pareja verifica con tu clave pública:

```bash
gpg --verify anuncio.txt.asc
```

✔ **Debería decir: "Good signature from ..."**

Ahora la prueba de integridad: editá el archivo `anuncio.txt.asc`
cambiando UNA letra del texto, volvé a verificar (`gpg --verify`)...
**falló. Cambió ni una coma y se detectó.** Esa es la integridad.

## ✅ Autodiagnóstico: si algo falla

| Problema | Solución |
|---|---|
| `gpg: no se encontró la clave pública` | El email no coincide con el importado. Mirá con `gpg --list-keys` qué email importaste. |
| No pasa nada al importar | Fijate que el archivo termine en `.asc` y que lo tengas en la carpeta actual (`ls`). |
| Pide la passphrase al descifrar | Normal: es la passphrase de TU clave (la escribiste al generar). Escríbela. |
| `No public key` al cifrar | Todavía no importaste la clave de tu pareja. Volvé al paso de `gpg --import`. |
| No me deja borrar la clave | Tenés que borrar la privada primero; usá el comando del cierre. |

## 🧹 Cierre — Higiene del llavero

Las claves de la clase son de práctica. Borralas al terminar:

```bash
gpg --list-keys           # anotá el identificador largo de cada clave
gpg --delete-secret-and-public-key "Mi Nombre"
```

> 💡 La higiene del llavero también se enseña: una clave sin uso que
> queda olvidada es un riesgo, no una reliquia.

## 🖼️ Opcional — Kleopatra (interfaz gráfica)

Si preferís ver un llavero visual en lugar del terminal, **Kleopatra**
(incluida con Gpg4win en Windows, disponible en los repos de Debian)
hace todo lo mismo:

- **Crear par de claves:** New Key Pair → Create → nombre y email.
- **Importar la de tu pareja:** Import → elegí el `.asc`.
- **Cifrar un archivo:** botón derecho sobre el archivo →
  Encrypt → elegí destinatario.
- **Descifrar:** doble click en el archivo `.asc` → Decrypt/Verify.

💡 Nuestra recomendación: usá la CLI (los comandos de arriba) durante
la práctica — es la misma en Windows, Linux y Mac, y te va a servir
en cualquier servidor o terminal de trabajo. Kleopatra queda como
herramienta de exploración al final de la clase.