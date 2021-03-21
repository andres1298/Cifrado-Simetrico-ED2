from cryptography.fernet import Fernet
import os
import sys
import time

KEY_NAME = 'key.key'
MESSAGE_NAME = 'message.encrypted'
SOURCE_FILE = 'message.txt'

# Se simula la carga
def loading(message):
    timer = 0
    loading = f'{message}: [-----------------]'
    backtrack = '\b' * len(loading)
    print(backtrack)

    while timer < len(loading) - 10:
        sys.stdout.write(backtrack + loading)
        sys.stdout.flush()
        loading = loading.replace("-", chr(9608), 1)
        time.sleep(0.15)
        timer += 1
    time.sleep(0.5)
    sys.stdout.write(backtrack)
    print(loading + " \n¡Listo!")


def generate_key():
    # Se genera una nueva llave utilizando la implementacion Fernet de AES
    key = Fernet.generate_key()
    return key


def save_file(file_name, content):
    # Se crea un archivo con la llave generada
    file = open(file_name, 'wb')
    file.write(content)
    file.close()


def get_message():
    data = input("Digite una frase oculta: ")
    return data


def get_message_from_file():
    if os.path.exists(SOURCE_FILE):
        with open(SOURCE_FILE, 'rb') as f:
            data = f.read()  # Read the bytes of the input file
        return data
    else:
        raise Exception('No se encontró el archivo original')


def mensaje_bienvenida():
    mensaje = '------------------------------\nSISTEMA DE CIFRADO DE MENSAJES\n------------------------------'
    print(mensaje)

def main():
    # Se obtiene un mensaje y se convierte en bytes
    try:
        mensaje_bienvenida()
        # message = get_message().encode()
        message = get_message_from_file()

        # Generacion de la llave
        loading('Generando llave')
        key = generate_key() # Se genera la llave privada para cifrar el archivo
        save_file(KEY_NAME, key) # Se guarda la llave
        f = Fernet(key)


        # Cifrado del mensaje
        loading('Cifrando mensaje')
        encrypted = f.encrypt(message)  # Se cifran los bytes del mensaje.
        save_file(MESSAGE_NAME, encrypted)  # Se guarda el mensaje

        print(f'\nEl mensaje cifrado se almacenó en \'{MESSAGE_NAME}\' y la llave en \'{KEY_NAME}\'.\nGuarde la llave en un directorio seguro.')
    except Exception as exc:
        print(f'Error al cifrar el mensaje: {exc}')


if __name__ == "__main__":
    main()