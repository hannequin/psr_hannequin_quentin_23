# Specification

Creer un systeme d'authentification qui utilise une connexion bluetooth d'un appareil mobile pour vérifier la presence de l'utilisateur pret du client.
Ce client une fois le mot de passe valider pourra ce connecter a une interface qui demandera les commandes docker a lancer.

## Contraintes

**Authentification Bluetooth** : Le programme devra être capable de communiquer avec un appareil mobile via Bluetooth pour vérifier la présence de l'utilisateur. Si l'utilisateur est présent, le programme devra récupérer les identifiants de l'utilisateur.

**Sécurité** : Le programme devra utiliser des protocoles de sécurité pour assurer l'authenticité et la confidentialité des données transmises via Bluetooth et pour protéger les identifiants des utilisateurs.

**Interface utilisateur** : Le programme devra offrir une interface utilisateur facile à utiliser pour les clients qui se connectent. Cette interface devra demander le nom du conteneur Docker à lancer.

**Validation de l'identité** : Le programme devra vérifier la validité des identifiants de l'utilisateur avant de lui permettre de se connecter. Si les identifiants ne sont pas valides, l'accès sera refusé.

**Lancement du conteneur Docker** : Une fois que les identifiants de l'utilisateur ont été validés et que le nom du conteneur Docker a été entré, le programme devra lancer le conteneur Docker demandé.

**Gestion des erreurs** : Le programme devra gérer les erreurs de manière appropriée en informant l'utilisateur des problèmes et des solutions possibles.

**Configurabilité** : Le programme devra être configurable en fonction des besoins de l'utilisateur, par exemple en permettant de changer les protocoles de sécurité utilisés ou en modifiant la façon dont l'interface utilisateur est présentée.

**Documentation** : Le programme devra être accompagné d'une documentation claire et détaillée pour aider les utilisateurs à comprendre comment l'utiliser et à résoudre les problèmes éventuels.

**Maintenance** : Le programme devra être facilement maintenable, avec un code propre et facilement compréhensible pour les développeurs (utilisation de la norme PEP8). Les mises à jour de sécurité devront être effectuées rapidement en cas de besoin.

**Compatibilité** : Le programme devra être compatible avec les systèmes d'exploitation et les plateformes mobiles les plus courants pour assurer une utilisation facile pour les clients.


# Contrat

## serveur_bluetooth

:pre-cond: adresse bluetooth du serveur et port défini
:pre-cond: carte bluetooth lancer

:sortie: Demande d'authentification à l'appareil connecter

:post-cond: la connexion reste tant que l'utilisateur ne rentre pas "exit" dans les commandes

:invariant: L'appareil connecter doit etre dans la liste défini

## client_bluetooth

:pre-cond: adresse bluetooth du serveur et port défini
:pre-cond: Carte bluetooth demarrer

:sortie: Affiche validation de connexion
:sortie: Recoit la demande d'authentification du serveur

:post-cond: la connexion reste tant que l'utilisateur ne rentre pas "exit" dans les commandes

## Authentification

:pre-cond: le serveur et le client sont connecter

:sortie: le serveur envoi la demande d'authentification

:post-cond: l'identifiant et le mot de passe sont contenu dans les fichiers correspondants

## commande_docker

:pre-cond: le serveur et le client sont connecter
:pre-cond: les identifiants sont valider

:sortie: demande de la commande docker a executer sur le serveur

:post-cond: la commande doit contenir "docker" et ne doit pas contenir "sudo"