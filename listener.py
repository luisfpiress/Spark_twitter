import socket
import time

HOST = 'localhost'
PORT = 3000

S = socket.socket()
S.bind((HOST,PORT))
print(f'Aguardando conexão na porta: {PORT}')

S.listen(5)
conn, address = S.accept()

print(f'recebendo solicitação de {address}')

messages = [
    'Mensagem A',
    'Mensagem B',
    'Mensagem C',
    'Mensagem D',
    'Mensagem E',
    'Mensagem F',

]

for menssage in messages:
    message = bytes(message, 'utf-8')
    conn.send(message)
    time.sleep(4)

conn.close