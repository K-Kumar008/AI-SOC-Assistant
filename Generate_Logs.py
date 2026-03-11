import random
from datetime import datetime, timedelta
import os

num_logs = 2000  # Total logs to generate
start_time = datetime(2026, 3, 11, 0, 0, 0)

brute_ips = ["192.168.1.10", "192.168.1.11"]
multiuser_ips = ["192.168.1.10", "192.168.1.11"]
portscan_ips = ["10.0.0.5", "172.16.0.3"]
users = ["root", "admin", "guest", "test", "user1"]
normal_ips = ["192.168.1.20", "192.168.1.21"]
normal_users = ["john", "alice", "bob"]
ports = list(range(20, 30))

os.makedirs("logs", exist_ok=True)

with open("logs/auth.log", "w") as f:
    for i in range(num_logs):
        log_time = start_time + timedelta(seconds=i*random.randint(1,5))
        time_str = log_time.strftime("%b %d %H:%M:%S")
        log_type = random.choices(
            ["bruteforce", "portscan", "multiuser", "normal"],
            weights=[0.25, 0.25, 0.25, 0.25],
            k=1
        )[0]

        if log_type == "bruteforce":
            ip = random.choice(brute_ips)
            user = random.choice(users[:2])
            port = random.choice(ports[:2])
            line = f"{time_str} kali sshd[1234]: Failed password for {user} from {ip} port {port} ssh2\n"
        elif log_type == "portscan":
            ip = random.choice(portscan_ips)
            user = random.choice(users[:2])
            port = random.choice(ports)
            line = f"{time_str} kali sshd[1234]: Failed password for {user} from {ip} port {port} ssh2\n"
        elif log_type == "multiuser":
            ip = random.choice(multiuser_ips)
            user = random.choice(users)
            port = random.choice(ports[:2])
            line = f"{time_str} kali sshd[1234]: Failed password for {user} from {ip} port {port} ssh2\n"
        else:
            ip = random.choice(normal_ips)
            user = random.choice(normal_users)
            port = random.choice(ports)
            status = random.choice(["Accepted password", "Failed password"])
            line = f"{time_str} kali sshd[1234]: {status} for {user} from {ip} port {port} ssh2\n"

        f.write(line)

print(f"Generated {num_logs} logs in logs/auth.log")
