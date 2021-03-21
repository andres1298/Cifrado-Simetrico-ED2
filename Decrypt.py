from cryptography.fernet import Fernet
import os

KEY_NAME = 'key.key'
MESSAGE_NAME = 'message.encrypted'

def get_key():
    file = open(KEY_NAME, 'rb')
    key = file.read()
    file.close()
    return key


def mensaje_bienvenida():
    mensaje = '------------------------------\nSISTEMA DE CIFRADO DE MENSAJES\n------------------------------\n'
    print(mensaje)


def main():
    mensaje_bienvenida()
    if os.path.exists(KEY_NAME):
        if os.path.exists(MESSAGE_NAME):

            with open(MESSAGE_NAME, 'rb') as f:
                data = f.read()  # Read the bytes of the encrypted file

            with open(KEY_NAME, 'rb') as f:
                try:
                    # do stuff
                    key = get_key()
                    f = Fernet(key)
                    decrypted = f.decrypt(data)

                    # Decode
                    original = decrypted.decode()
                    print(original)

                except:  # whatever reader errors you care about
                    print('Error al encriptar el archivo')
        else:
            print('No se pudo encontrar el mensaje por descifrar')

    else:
        print('No se pudo encontrar la llave de cifrado')

if __name__ == "__main__":
    main()