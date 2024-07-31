FROM alpine:3.19

RUN apk add --update --no-cache \
    gcc \
    python3 \
    py3-pip\
 && pip install --break-system-packages \
    "ruamel.yaml<0.18.0"
