"""Démarrage de l'add-on : lit les options HA, récupère le serveur MQTT, lance Ocean2MQTT."""

import json
import os
import sys
import urllib.request

OPTIONS = "/data/options.json"


def log(msg: str) -> None:
    print(f"[ocean2mqtt-addon] {msg}", flush=True)


def mqtt_from_supervisor() -> dict:
    token = os.environ.get("SUPERVISOR_TOKEN")
    if not token:
        return {}
    req = urllib.request.Request(
        "http://supervisor/services/mqtt", headers={"Authorization": f"Bearer {token}"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.load(resp).get("data") or {}
    except Exception as err:  # noqa: BLE001
        log(f"Serveur MQTT introuvable via le Supervisor ({err}). Installez l'add-on Mosquitto "
            "ou renseignez mqtt_host dans la configuration.")
        return {}


def main() -> None:
    try:
        with open(OPTIONS, encoding="utf-8") as f:
            opts = json.load(f)
    except FileNotFoundError:
        opts = {}

    env = {
        "SERIAL_PORT": opts.get("serial_port", "/dev/ttyUSB0"),
        "MQTT_TOPIC_NAME": opts.get("topic_name", "name"),
        "FRONTEND_HOST": "0.0.0.0",
        "FRONTEND_PORT": 8080,
        "RECOM_ENABLED": bool(opts.get("recom", True)),
    }

    if opts.get("mqtt_host"):
        env["MQTT_HOST"] = opts["mqtt_host"]
        env["MQTT_PORT"] = opts.get("mqtt_port") or 1883
        if opts.get("mqtt_user"):
            env["MQTT_USERNAME"] = opts["mqtt_user"]
            env["MQTT_PASSWORD"] = opts.get("mqtt_password") or ""
        log(f"Serveur MQTT (configuration) : {env['MQTT_HOST']}:{env['MQTT_PORT']}")
    else:
        svc = mqtt_from_supervisor()
        if svc:
            env["MQTT_HOST"] = svc.get("host")
            env["MQTT_PORT"] = svc.get("port", 1883)
            env["MQTT_USERNAME"] = svc.get("username")
            env["MQTT_PASSWORD"] = svc.get("password")
            env["MQTT_TLS"] = bool(svc.get("ssl"))
            log(f"Serveur MQTT (Supervisor) : {env['MQTT_HOST']}:{env['MQTT_PORT']}")

    # Configuration de Home Assistant (lecture seule) : reprise depuis NodOcean for HA
    for ha_dir in ("/homeassistant", "/config"):
        if os.path.isdir(os.path.join(ha_dir, ".storage")):
            env["HOMEASSISTANT_CONFIG_DIR"] = ha_dir
            break

    if opts.get("web_password"):
        env["FRONTEND_PASSWORD"] = opts["web_password"]

    # Les valeurs sont relues en YAML par Ocean2MQTT : JSON garde les chaînes en chaînes.
    for key, value in env.items():
        if value is not None:
            os.environ[f"OCEAN2MQTT_{key}"] = json.dumps(value)

    args = [sys.executable, "-m", "ocean2mqtt", "--data", "/data/ocean2mqtt"]
    if opts.get("log_level") == "debug":
        args.append("-v")
    log(f"Clé EnOcean : {env['SERIAL_PORT']}")
    os.execvp(args[0], args)


if __name__ == "__main__":
    sys.exit(main())
