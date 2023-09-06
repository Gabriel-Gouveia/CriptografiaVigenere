from socket import *

def descriptografa_vigenere(cifra, chave):
    mensagemDescriptografada = ""
    tamanhoChave = len(chave)
    for i in range(len(cifra)):
        char = cifra[i]
        if char.isalpha():
            chaveChar = chave[i % tamanhoChave]
            shift = ord(chaveChar) - ord('a')
            if char.isupper():
                charDescriptografado = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                charDescriptografado = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            mensagemDescriptografada += charDescriptografado
        else:
            mensagemDescriptografada += char
    return mensagemDescriptografada

serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print("UDP server\n")

while True:
    messagem, clientAddress = serverSocket.recvfrom(2048)
    texto = str(messagem, "utf-8") 

    chave = input("Insira a chave Vigenére para a descriptografia: ") 
    MensagemDescriptografada = descriptografa_vigenere(texto, chave)
    
    print("Mensagem recebida: ", MensagemDescriptografada)
