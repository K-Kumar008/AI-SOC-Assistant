from parser.log_parser import parse_auth_log
from detection.advanced_detector import detect_bruteforce, detect_portscan, detect_multiuser_attempts
from reports.report_generator import generate_report
from ai_analysis.llm_analyzer import analyze_alerts

# 1. Parse logs
events = parse_auth_log("logs/auth.log")

# 2. Run detection
alerts = []
alerts += detect_bruteforce(events)
alerts += detect_portscan(events)
alerts += detect_multiuser_attempts(events)

# 3. Generate report
report = generate_report(alerts)
print(report)
with open("reports/incident_report.txt", "w") as f:
    f.write(report)

# 4. AI analysis
ai_report = analyze_alerts(alerts)
print("\nAI Threat Analysis:\n")
print(ai_report)
with open("reports/ai_analysis.txt", "w") as f:
    f.write(ai_report)
