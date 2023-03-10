import socket

# Adresse du serveur Bluetooth à connecter
serveur_adresse = 'localhost'
# Port à utiliser pour la connexion
port = 1234

# Création du socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect((serveur_adresse, port))

# Envoi de données au serveur
message = b"Hello, world!"
client_socket.sendall(message)

# Réception des données du serveur
data = client_socket.recv(1024)
print("Reçu:", data)

# Fermeture de la connexion
client_socket.close()

