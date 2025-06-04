# On part de l'image de base Telegraf (version Debian)
FROM telegraf:1.34

# On passe en utilisateur root pour installer des paquets
USER root

# On enchaîne toutes les commandes avec "&&" pour s'assurer
# que si l'une échoue, tout s'arrête.
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install requests rich --break-system-packages && \
    rm -rf /var/lib/apt/lists/*

# On repasse à l'utilisateur par défaut de Telegraf pour la sécurité
# (Cette commande doit être seule sur sa ligne)
USER telegraf