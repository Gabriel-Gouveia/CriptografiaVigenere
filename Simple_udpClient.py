from socket import *

def criptografar_vigenere(plain_text, key):
    texto_criptografado = ""
    tamanhoDaChave = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            chave_char = key[i % tamanhoDaChave]
            shift = ord(chave_char) - ord('a')
            if char.isupper():
                charCriptografado = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                charCriptografado = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            texto_criptografado += charCriptografado
        else:
            texto_criptografado += char
    return texto_criptografado

serverName = "127.0.0.1"
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("UDP Client\n")

while True:
    mensagem = input("Digite uma mensagem: ")
    if mensagem == "sair":
        break

    chave = input("Insira a chave Vigenère: ")
    mensagemCriptografada = criptografar_vigenere(mensagem, chave)
    
    clientSocket.sendto(bytes(mensagemCriptografada, "utf-8"), (serverName, serverPort))

clientSocket.close()
