# AI SOC Assistant

## Overview

AI SOC Assistant is a Python-based Security Operations Center (SOC) automation tool that analyzes Linux authentication logs to detect potential cyber attacks.
The system parses log files, applies detection rules, generates SOC-style incident reports, and optionally performs AI-based threat analysis.

This project simulates how SOC analysts monitor logs and identify suspicious activity.

---

## Features

* Log Parsing from Linux authentication logs
* Brute Force Attack Detection
* Port Scan Detection
* Multiple User Login Attempt Detection
* SOC Incident Report Generation
* Optional AI-based threat explanation
* Synthetic log generation for testing

---

## Project Architecture

Logs → Parser → Detection Engine → Report Generator → AI Analysis

---

## Folder Structure

ai-soc-assistant/

detection/ → attack detection rules
parser/ → log parsing module
ai_analysis/ → AI threat analysis
logs/ → authentication log files
reports/ → generated SOC reports
screenshots/ → project screenshots

generate_logs.py → generates test logs
main.py → main execution script

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/ai-soc-assistant.git
cd ai-soc-assistant
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

### 1 Generate sample logs

```
python3 generate_logs.py
```

This creates synthetic authentication logs in the logs directory.

### 2 Run the SOC assistant

```
python3 main.py
```

The program will:

1. Parse log entries
2. Detect suspicious activity
3. Generate a SOC incident report
4. Optionally run AI threat analysis

---

## Example Output

SOC Incident Report

Threat Type: Brute Force Attack
Source IP: 192.168.1.10
Attempts: 7

Threat Type: Multi-user Login Attempts
Source IP: 192.168.1.11
Users Tried: root, admin, guest

---

## Screenshots

### Folder Structure

(Add screenshot here)

### Sample Logs

(Add screenshot here)

### Incident Report

(Add screenshot here)

### AI Analysis

(Add screenshot here)

---

## Technologies Used

Python
Regular Expressions
Log Analysis
OpenAI API (optional)

---

## Future Improvements

Real-time log monitoring
Integration with SIEM tools
Email alert system
MITRE ATT&CK mapping
Web dashboard for SOC monitoring

---

## Author

Krishna
Cybersecurity Enthusiast



