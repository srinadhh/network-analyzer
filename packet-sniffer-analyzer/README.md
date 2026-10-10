# Packet Sniffer Analyzer

Packet Sniffer Analyzer is a Python-based packet sniffer and protocol analyzer scaffold for a computer networks university project. It is intended to use Scapy for live capture and offline PCAP analysis while supporting protocol/IP/port filtering, traffic statistics, and optional visualization/detection extensions.

## Feature checklist

- [ ] Live packet capture
- [ ] Read packets from PCAP
- [ ] Save packets to PCAP
- [ ] Parse packets into structured dictionaries
- [ ] Filter by protocol, IP, and port
- [ ] Protocol distribution and top talkers statistics
- [ ] Packets-per-second metric
- [ ] Port scan and ARP spoof detection (stretch goal)
- [ ] Protocol distribution plotting (stretch goal)

## Setup

1. Create and activate a virtual environment:
   - Linux/macOS:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Packet capture privileges:
   - Windows: install Npcap (WinPcap-compatible mode recommended).
   - Linux/macOS: run with `sudo` (or equivalent capability setup) for live capture.

## Usage examples

```bash
python main.py --list-interfaces
python main.py -i eth0 -c 100 --protocol TCP --save captures/session.pcap
python main.py --read captures/session.pcap --stats
```

## Project structure

```text
packet-sniffer-analyzer/
├── sniffer/
├── tests/
├── captures/
├── docs/
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Ethical use

Only capture traffic on networks and systems you own or have explicit permission to monitor.
