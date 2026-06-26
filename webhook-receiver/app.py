from flask import Flask, request, jsonify
from datetime import datetime
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

alert_history = []


@app.route("/", methods=["POST"])
def receive_alert():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    received_at = datetime.utcnow().isoformat() + "Z"
    alerts = data.get("alerts", [])

    for alert in alerts:
        name = alert.get("labels", {}).get("alertname", "Unknown")
        status = alert.get("status", "unknown")
        severity = alert.get("labels", {}).get("severity", "none")
        summary = alert.get("annotations", {}).get("summary", "No summary")
        instance = alert.get("labels", {}).get("instance", "unknown")

        log_msg = f"[{status.upper()}] {name} | severity={severity} | instance={instance} | {summary}"
        if status == "firing":
            logger.warning(log_msg)
        else:
            logger.info(log_msg)

        alert_history.append({
            "received_at": received_at,
            "name": name,
            "status": status,
            "severity": severity,
            "instance": instance,
            "summary": summary,
        })

    # Keep last 100 alerts only
    if len(alert_history) > 100:
        alert_history[:] = alert_history[-100:]

    return jsonify({"status": "ok", "alerts_received": len(alerts)}), 200


@app.route("/alerts", methods=["GET"])
def list_alerts():
    return jsonify({
        "total": len(alert_history),
        "alerts": list(reversed(alert_history)),
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
