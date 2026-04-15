# Simple Port Scanner  
  
A lightweight multithreaded Python port scanner for checking open TCP ports on a target IP address within a specified range.  
  
---  
## Features  
  
- Scan any IPv4 address  
- Custom port range input  
- Multithreaded scanning for faster execution  
- Thread safety using locks and semaphores  
- Simple CLI-based interaction  
- Lightweight (no external dependencies)  
---  
  
## Usage  
  
Run the script:  
  
```bash  
python port_scanner.py
```

Followed by interactive input prompts
```
Enter the target IP address: 192.168.1.1
Enter the port range (e.g., 20-100): 1-1024
```
---
## Example output
```
Scanning 192.168.1.1 from port 1 to 1024...

[OPEN] Port 22
[OPEN] Port 80
[OPEN] Port 443

Scan complete.

Open ports: [22, 80, 443]
```
---
## Architecture

- Thread-per-port scanning model
- `socket.connect()` used for TCP reachability check
- `threading.Semaphore` limits active threads
- `threading.Lock` ensures safe shared state updates
- Timeout-based detection (0.3s per port)
---
## How it works

For each port in the given range:

1. A thread attempts TCP connection to `(IP, port)`
2. If connection succeeds → port is considered open
3. If timeout or error → port is closed/filtered
4. Results are stored in a shared list safely using a lock
---
## Limitations

- Not optimized for very large port ranges (10k+ ports → heavy threading)
- No async I/O (uses thread-based concurrency)
- Does not detect UDP ports
- Firewall may cause false negatives
- Scan speed depends on network latency and timeout value
---
## Security Note

This tool is intended for educational and authorized testing purposes only.  
Do not scan systems without permission.

---
## Requirements

- Python 3.8+
- Standard library only (socket, threading, ipaddress)
---
## Motivation

This project was created to practice low-level network interaction concepts in Python.

It focuses on:
- understanding TCP connection behavior
- thread-based concurrency control
- safe shared-state manipulation
- building CLI-driven diagnostic tools

The goal is not to replace professional scanners, but to understand how port discovery works at a fundamental level.
