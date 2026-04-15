import socket
import threading
import ipaddress

lock = threading.Lock()
MAX_THREADS = 250  # limit the number of threads - edit if needed
semaphore = threading.Semaphore(MAX_THREADS) # limit threads for optimization
open_ports = []  # list to store open ports
# === PORT SCANNING FUNCTION ===
def scan(target, port):
    with semaphore:  # execute with available threads
    # if problem occurs "with semaphore:" use .acquire() and .release() instead for accuracy (less safe but faster)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)

        try:
            s.connect((target, port))
            with lock: # if problem occurs "with lock:" use .acquire() and .release() instead for accuracy (less safe but faster)
                print(f"[OPEN] Port {port}")
                open_ports.append(port)
        except (socket.timeout, socket.error):
            pass
        finally:
            s.close()

if __name__ == "__main__":
    # --- INPUT: IP ---
    while True:
        target = input("Enter the target IP address: ")
        try:
            ipaddress.ip_address(target)
            break
        except ValueError:
            print("Invalid IP address. Please try again.")


    # --- INPUT: PORT RANGE ---

    while True:
        set_range = input("Enter the port range (e.g., 20-100): ")

        try:
            parts = set_range.split('-')
            if len(parts) != 2:
                raise ValueError

            start_port, end_port = map(int, parts)

            if 0 <= start_port <= 65535 and 0 <= end_port <= 65535 and start_port <= end_port:
                break
            else:
                print("Port numbers must be between 0 and 65535.")

        except ValueError:
            print("Invalid format. Use start-end.")


    # --- SCANNING ---
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScan complete.\n")
    print(f"Open ports on {target} in range {start_port}-{end_port}: {open_ports if open_ports else 'None'}")