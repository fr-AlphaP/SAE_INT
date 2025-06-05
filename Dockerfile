FROM telegraf:1.34

USER root

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install requests rich --break-system-packages && \
    rm -rf /var/lib/apt/lists/*

USER telegraf