import socket

# Adresse MAC du serveur Bluetooth
server_addr = 'B8:31:B5:74:6B:66'
# Canal utilisé pour la connexion
port = 4

# Création de la socket du client Bluetooth
client_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Connexion au serveur Bluetooth
client_sock.connect((server_addr, port))

# Envoyer des données au serveur
client_sock.send("Hello, serveur!")

# Recevoir des données du serveur
data = client_sock.recv(1024)
print("Received:", data)

# Fermer la socket du client
client_sock.close()
