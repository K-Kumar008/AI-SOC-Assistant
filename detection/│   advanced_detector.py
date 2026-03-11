from collections import defaultdict

# Thresholds
BRUTE_FORCE_THRESHOLD = 5
PORT_SCAN_THRESHOLD = 10
MULTIUSER_THRESHOLD = 3

def detect_bruteforce(events):
    alerts = []
    counter = defaultdict(int)
    for e in events:
        if e["status"] == "Failed":
            counter[e["ip"]] += 1
    for ip, attempts in counter.items():
        if attempts >= BRUTE_FORCE_THRESHOLD:
            alerts.append({"type": "Brute Force Attack", "ip": ip, "attempts": attempts})
    return alerts

def detect_portscan(events):
    alerts = []
    ports_per_ip = defaultdict(set)
    for e in events:
        ports_per_ip[e["ip"]].add(e["port"])
    for ip, ports in ports_per_ip.items():
        if len(ports) >= PORT_SCAN_THRESHOLD:
            alerts.append({"type": "Port Scan", "ip": ip, "ports_scanned": list(ports)})
    return alerts

def detect_multiuser_attempts(events):
    alerts = []
    users_per_ip = defaultdict(set)
    for e in events:
        if e["status"] == "Failed":
            users_per_ip[e["ip"]].add(e["user"])
    for ip, users in users_per_ip.items():
        if len(users) >= MULTIUSER_THRESHOLD:
            alerts.append({"type": "Multi-user Login Attempts", "ip": ip, "users_tried": list(users)})
    return alerts
