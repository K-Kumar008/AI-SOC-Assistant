def generate_report(alerts):
    report = "SOC Incident Report\n"
    report += "Generated: 2026-03-11\n"
    report += "-"*40 + "\n\n"

    for alert in alerts:
        report += f"Threat Type : {alert['type']}\n"
        report += f"Source IP   : {alert['ip']}\n"
        if alert['type'] == "Brute Force Attack":
            report += f"Attempts    : {alert['attempts']}\n"
        elif alert['type'] == "Port Scan":
            report += f"Ports Scanned : {alert['ports_scanned']}\n"
        elif alert['type'] == "Multi-user Login Attempts":
            report += f"Users Tried : {alert['users_tried']}\n"
        report += "\n"
    return report
