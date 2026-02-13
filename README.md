# Scam Investigation Toolset

This repository provides a set of tools and documentation for analyzing employment scams, with a focus on domain masquerading and infrastructure attribution. These resources were developed to document the tactics used by groups impersonating legitimate technology companies.

## Disclaimer
This project is for educational and investigative use only. Interacting with fraudulent actors involves risk. Never provide actual personal information, bank details, or sensitive documents. It is recommended to run these tools in a secure, isolated environment.

## Tools and Features

### 1. Honey-pot Tracker (tracker.py)
A Python-based server that logs metadata from connection attempts. It is designed to capture the IP address, device type (User-Agent), and referring headers of anyone who accesses the link.
*   **Application:** When a scammer requests signed documents or ID verification, you can provide a link (proxied through a tool like ngrok) to this server.
*   **Logging:** All visitor data is saved to a local log file for analysis and reporting to ISPs or law enforcement.

### 2. Investigation Framework
The project outlines a systematic approach to verifying a recruitment process:
*   **Domain Analysis:** Checking the registration age and history of the sender's domain.
*   **Infrastructure Audit:** Comparing the DNS configuration (MX, SPF, and TXT records) of the suspicious domain against the legitimate company's official records.
*   **Cloud Project Identification:** Identifying unique Google Cloud Project numbers from email headers to link different scam campaigns.
*   **Metadata Comparison:** Cross-referencing marketing names (e.g., "QuantumPulse" vs. "AutoPilot") used by scammers against official company products.

## Setup and Usage
This project uses the 'uv' package manager for Python.

```bash
# To start the tracking server
uv run tracker.py
```

To make the server accessible over the internet for an investigation, use a tunneling service like ngrok to forward traffic to port 8080.

## Project Structure
- tracker.py: The tracking server script.
- private/: A directory (excluded from git) for storing sensitive email headers, investigator reports, and personal notes.
- pyproject.toml: Project dependencies and configuration.

## Reporting
The goal of this project is to produce high-quality evidence that can be submitted to:
- Domain registrars (Abuse departments)
- Google Cloud Abuse teams
- The FBI IC3 (Internet Crime Complaint Center)
