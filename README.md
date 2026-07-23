# CodeAlpha - Basic Network Sniffer (Task 1)

This project is a **Basic Network Sniffer** developed as part of the Cybersecurity Internship at **CodeAlpha**. The program captures live network traffic packets and displays essential protocol and payload information.

---

## 🚀 Features
* Captures network packets in real-time.
* Extracts and displays:
  * **Source IP Address**
  * **Destination IP Address**
  * **Protocol Type**
  * **Packet Payload (Data)**

---

## 🛠️ Prerequisites & Requirements
Before running the script, ensure you have the following installed:
1. **Python** (v3.x recommended)
2. **Npcap** (Required for Windows to capture raw packets; make sure to check "Install Npcap in WinPcap API-compatible Mode" during installation).
3. **Scapy Library**

---

## 📦 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/CodeAlpha_BasicNetworkSniffer.git](https://github.com/YOUR_USERNAME/CodeAlpha_BasicNetworkSniffer.git)
   cd CodeAlpha_BasicNetworkSniffer


   # Task 3: OWASP Juice Shop - SQL Injection Remediation

### Overview
In this task, the SQL Injection (SQLi) vulnerability identified in the OWASP Juice Shop application (specifically within the login endpoint) was successfully remediated. 

### Key Actions Performed:
* **Vulnerability Identification:** Located the vulnerable code block where user inputs (`email` and `password`) were directly concatenated into the SQL query string, allowing attackers to bypass authentication.
* **Code Refactoring:** Replaced the insecure string concatenation approach with **Parameterized Queries (Prepared Statements)** using placeholders (`?`). This ensures that user-supplied input is strictly treated as data rather than executable database commands.
* **Security Verification:** Tested the updated backend logic to ensure that authentication forms are protected against malicious SQL syntax injections while maintaining normal user login functionality.
