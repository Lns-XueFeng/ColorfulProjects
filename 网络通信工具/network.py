import tkinter as tk
from tkinter import ttk
import socket
import subprocess
import threading


def port_scanner():
    host = host_entry.get()
    ports = [int(port) for port in ports_entry.get().split(",")]
    open_ports = []

    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            pass

    for port in ports:
        threading.Thread(target=scan_port, args=(port,)).start()

    root.after(100, update_port_scan_status, open_ports)


def update_port_scan_status(open_ports):
    status_label.config(text=f"Open ports: {', '.join(map(str, open_ports))}")


def ping():
    host = ping_host_entry.get()
    try:
        output = subprocess.check_output(["ping", "-c", "4", host])
        status_label.config(text="Host is reachable.")
    except subprocess.CalledProcessError:
        status_label.config(text="Host is unreachable.")


def clear_ping_status():
    status_label.config(text="")


def udp_client():
    host = udp_host_entry.get()
    port = int(udp_port_entry.get())
    message = udp_message_entry.get()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode(), (host, port))
        data, addr = sock.recvfrom(1024)
        sock.close()
        status_label.config(text=f"Received response from UDP server: {data.decode()}")
    except Exception as e:
        status_label.config(text=f"UDP Error: {str(e)}")


def clear_udp_status():
    status_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Network Tool")

    # Port Scanner
    port_scanner_frame = ttk.LabelFrame(root, text="Port Scanner")
    port_scanner_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    host_label = ttk.Label(port_scanner_frame, text="Host:")
    host_label.grid(row=0, column=0, padx=5, pady=5)
    host_entry = ttk.Entry(port_scanner_frame)
    host_entry.grid(row=0, column=1, padx=5, pady=5)

    ports_label = ttk.Label(port_scanner_frame, text="Ports (comma-separated):")
    ports_label.grid(row=1, column=0, padx=5, pady=5)
    ports_entry = ttk.Entry(port_scanner_frame)
    ports_entry.grid(row=1, column=1, padx=5, pady=5)

    scan_button = ttk.Button(port_scanner_frame, text="Scan Ports", command=port_scanner)
    scan_button.grid(row=2, columnspan=2, padx=5, pady=5)

    # Ping
    ping_frame = ttk.LabelFrame(root, text="Ping")
    ping_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    ping_host_label = ttk.Label(ping_frame, text="Host:")
    ping_host_label.grid(row=0, column=0, padx=5, pady=5)
    ping_host_entry = ttk.Entry(ping_frame)
    ping_host_entry.grid(row=0, column=1, padx=5, pady=5)

    ping_button = ttk.Button(ping_frame, text="Ping", command=ping)
    ping_button.grid(row=1, column=0, padx=5, pady=5)
    clear_ping_button = ttk.Button(ping_frame, text="Clear", command=clear_ping_status)
    clear_ping_button.grid(row=1, column=1, padx=5, pady=5)

    # UDP Client
    udp_client_frame = ttk.LabelFrame(root, text="UDP Client")
    udp_client_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    udp_host_label = ttk.Label(udp_client_frame, text="Host:")
    udp_host_label.grid(row=0, column=0, padx=5, pady=5)
    udp_host_entry = ttk.Entry(udp_client_frame)
    udp_host_entry.grid(row=0, column=1, padx=5, pady=5)

    udp_port_label = ttk.Label(udp_client_frame, text="Port:")
    udp_port_label.grid(row=1, column=0, padx=5, pady=5)
    udp_port_entry = ttk.Entry(udp_client_frame)
    udp_port_entry.grid(row=1, column=1, padx=5, pady=5)

    udp_message_label = ttk.Label(udp_client_frame, text="Message:")
    udp_message_label.grid(row=2, column=0, padx=5, pady=5)
    udp_message_entry = ttk.Entry(udp_client_frame)
    udp_message_entry.grid(row=2, column=1, padx=5, pady=5)

    udp_send_button = ttk.Button(udp_client_frame, text="Send UDP Message", command=udp_client)
    udp_send_button.grid(row=3, column=0, padx=5, pady=5)

    clear_udp_button = ttk.Button(udp_client_frame, text="Clear", command=clear_udp_status)
    clear_udp_button.grid(row=3, column=1, padx=5, pady=5)

    # Status Label
    status_label = ttk.Label(root, text="")
    status_label.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    root.mainloop()
