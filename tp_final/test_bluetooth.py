""" 
    Test si l'appareil bluetooth est connecter et lance une connexion au serveur
"""
import bluetooth

# Recherche des appareils Bluetooth
devices = bluetooth.discover_devices()

# Afficher la liste des appareils Bluetooth
for addr in devices:
    print("Device:", addr, bluetooth.lookup_name(addr))

allowed_address = "12:34:56:78:90:AB"

devices = bluetooth.discover_devices()

if allowed_address in devices:
    print("Device found. Connecting to socket server...")
    serveur_adresse = 'localhost'
    # Port à utiliser pour la connexion
    port = 1234

    # Création du socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connexion au serveur
    client_socket.connect((serveur_adresse, port))

    username = input("Entrez votre nom d'utilisateur : ")
    password = input("Entrez votre mot de passe : ")
    
    # Envoyer les données au serveur
    client_socket.sendall(username.encode())
    client_socket.sendall(password.encode())

    # Attendre la réponse du serveur
    response = client_socket.recv(1024).decode()
    if response == "Connexion reussie":
        while docker_command != "exit":
            docker_command = input('Enter Docker command: ')
            client_socket.sendall(docker_command.encode())
            client_socket.recv(1024).decode()

    # Fermeture de la connexion
    client_socket.close()



else:
    print("Device not found. Socket client could not connect to server.")