import re

def parse_auth_log(file_path):
    events = []
    pattern = re.compile(
        r'(\w+ \d+ \d+:\d+:\d+) kali sshd\[\d+\]: (Failed|Accepted) password for (\w+) from (\d+\.\d+\.\d+\.\d+) port (\d+) ssh2'
    )
    with open(file_path, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                events.append({
                    "timestamp": match.group(1),
                    "status": match.group(2),
                    "user": match.group(3),
                    "ip": match.group(4),
                    "port": int(match.group(5))
                })
    return events
