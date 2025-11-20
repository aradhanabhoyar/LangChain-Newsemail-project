# generator/analytics.py
import json, os, datetime
ANALYTICS_FILE = "analytics.json"

def log_generation(run_id: str, sections: dict, subjects: list, total_sent: int):
    entry = {
        "run_id": run_id,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "sections": {k: len(v) for k, v in sections.items()},
        "subjects": subjects,
        "total_articles": sum(len(v) for v in sections.values()),
        "total_sent": total_sent
    }
    data = []
    if os.path.exists(ANALYTICS_FILE):
        try:
            with open(ANALYTICS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []
    data.append(entry)
    with open(ANALYTICS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return entry
