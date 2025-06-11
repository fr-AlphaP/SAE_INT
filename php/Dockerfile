FROM php:fpm-alpine

RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    build-base

RUN pip3 install --no-cache-dir \
    requests \
    rich \
    httpx \
    python-telegram-bot \
    nest_asyncio \
    --break-system-packages
