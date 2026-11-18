# Image de l'add-on Ocean2MQTT, construite par GitHub Actions pour chaque architecture
# (ghcr.io/ehomelabs/{arch}-addon-ocean2mqtt). Le paquet Ocean2MQTT (interface web et
# fiches produits incluses) vient de la release GitHub correspondante.
FROM python:3.13-slim

ARG OCEAN2MQTT_VERSION
ARG BUILD_ARCH=amd64

RUN python3 -m pip install --no-cache-dir \
    "https://github.com/eHomeLabs/Ocean2MQTT/releases/download/v${OCEAN2MQTT_VERSION}/ocean2mqtt-${OCEAN2MQTT_VERSION}-py3-none-any.whl"

COPY run.py /run.py

LABEL io.hass.version="${OCEAN2MQTT_VERSION}" \
      io.hass.type="addon" \
      io.hass.arch="${BUILD_ARCH}" \
      org.opencontainers.image.source="https://github.com/eHomeLabs/hassio-ocean2mqtt" \
      org.opencontainers.image.description="Add-on Home Assistant Ocean2MQTT" \
      org.opencontainers.image.licenses="MIT"

CMD ["python3", "-u", "/run.py"]
