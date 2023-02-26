import socket
import tweepy

HOST = 'localhost'
PORT = 9009

s  = socket.socket()
s.bind(HOST, PORT)
print('Aguardando conexão na porta: {PORT}')

s.listen(5)
connection, address = s.accept()
print('Recebendo solicitação de {address}')

token ='AAAAAAAAAAAAAAAAAAAAAF1GlQEAAAAAbAR7M7BjArNz%2FoAPn4FFeiuEz94%3D0374ctEP0xzPMz3N6f5UHd0uw6ZYovvJ8qLjhDSIAr5rJnSmN0'
keyword = 'bbb'

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        connection.send(tweet.text.encode('latin1', 'ignore'))

printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()

connection.close()