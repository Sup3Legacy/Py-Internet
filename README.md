# Py-Internet
Structure de réseau.

Les utilisateurs du réseau sont les pairs, qui communiquent avec les autres via leurs sockets, repérés par la combination de leur adresse IP et d'un port qu'ils allouent.

# Introduction
J'ai été inspiré par des lectures d'articles expliquant en détail le fonctionnement de réseaux type réseaux locaux/internet, et j'ai voulu simuler le fonctionnement d'un réseau. Pour cela, j'ai du bien sûr adapter et simplifier un peu les protocoles existants.

# Cheminement
Pour commencer, j'ai créé des premières structures de base, celles de pair, de paquet, de socket et de DNS. Puis je leur ai rajouté des méthodes permettant d'interragir.

Par exemple, l'envoi d'un paquet se passe de cette façon :
* Le programme qui doit envoyer un paquet l'ajoute à la file de paquets à envoyer du pair P_1 auquel il est rattaché
* Ce dernier interrroge le DNS, qui lui donne l'adresse IP du pair P_2 correspondant au nom (URL en fait) demandé
* Avec cette URL, P_1 envoie une demande de port à P_2
* P_2 lui affecte, pour la durée del'échange, un port libre ou en ouvre un nouveau (ou alros répond qu'il n'a aucun port libre)
* P_1 ajoute au socket (ie. port distant) donné le paquet.
* Le socket décompose le paquet et ajoute ses données dans la file des paquets reçus de P_2. Ce données peuvent alors être utilisées par le programme rattaché à P_2 à qui il est adressé.

# Pistes pour la suite
Je pense qu'il serait une bonne idée d'ajouter la possibiltié que les paquets voyagent entre les pairs comme sur un graphe, c'est-à-dire qu'il n'aillent pas directement de l'expéditeur au destinataire mais qu'il soient relayés par d'autres pairs.
