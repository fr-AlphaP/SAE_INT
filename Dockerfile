# On part de l'image de base Telegraf (version Debian)
FROM telegraf:1.34

# On passe en utilisateur root pour installer des paquets
USER root

# On installe pip, puis on force pip à installer requests en ignorant la protection
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install requests --break-system-packages && \
    rm -rf /var/lib/apt/lists/*

# On repasse à l'utilisateur par défaut de Telegraf pour la sécurité
USER telegraf