"""
    Creation socket bluetooth
"""
import socket

# Adresse MAC de l'appareil Bluetooth à connecter
#baddr = 'B8:31:B5:74:6B:66'
serveur_adresse = 'localhost'
# Canal à utiliser pour la connexion
port = 1234

# Création de la socket du serveur Bluetooth
# Non fonctionnel du a une erreure non trouver, mise en place de la connexion en ip pour les test
#server_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket du serveur au port et à l'adresse MAC
server_socket.bind((serveur_adresse, port))

# Mise en écoute du socket du serveur
server_socket.listen(1)

print("En attente de connexion Bluetooth...")

# Accepter la connexion du client
client_sock, client_info = server_socket.accept()
print("Connexion acceptée depuis", client_info)

while True:
    try:
        # Recevoir des données du client
        data = client_sock.recv(1024)
        if not data:
            # Si aucune donnée n'est reçue, la connexion est inactive
            print("Connexion Bluetooth inactive")
            break
        print("Recu:", data)
        
    # Envoyer des données au client
    # Demande d'authentification
        client_socket.sendall("Entrez votre nom d'utilisateur : ")
        username = client_socket.recv(1024).decode().strip()
        client_socket.sendall("Entrez votre mot de passe : ")
        password = client_socket.recv(1024).decode().strip()

        # Validation des identifiants
        with open('identifiant.txt', 'r') as f:
            usernames = [line.strip() for line in f]
        # Lire les mots de passe à partir d'un fichier
        with open('motdepasse.txt', 'r') as f:
            passwords = [line.strip() for line in f]  

        if username in usernames and password == passwords[usernames.index(username)]:
            print("Connexion reussie!")
            client_socket.sendall("Connexion reussie")
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")

    except Exception as e:
        print("Erreur de connexion Bluetooth :", e)
        break

# Fermer les sockets client et serveur
client_socket.close()
#server_socket.close()
