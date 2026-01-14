#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Найшвидший спосіб отримати пароль WiFi
Просто запустіть: python wifi-fast.py "TP-Link_284_5G"
"""

import subprocess
import sys
from datetime import datetime

def get_password(ssid):
    """Отримує пароль WiFi найшвидшим способом"""
    try:
        # Перевіряємо збережені паролі в Windows
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'profile', f'name={ssid}', 'key=clear'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        
        if result.returncode != 0:
            return None
        
        output = result.stdout
        
        # Шукаємо пароль
        for line in output.split('\n'):
            if 'Key Content' in line or 'Содержимое ключа' in line or 'Вміст ключа' in line:
                parts = line.split(':')
                if len(parts) > 1:
                    password = parts[1].strip()
                    if password:
                        return password
        
        # Перевіряємо відкриту мережу
        if 'Open' in output or 'Відкрита' in output:
            return "(Open Network - No Password)"
        
        return None
    except:
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python wifi-fast.py \"SSID\"")
        print("Example: python wifi-fast.py \"TP-Link_284_5G\"")
        sys.exit(1)
    
    ssid = sys.argv[1]
    print(f"Getting password for: {ssid}\n")
    
    password = get_password(ssid)
    
    if password:
        # Зберігаємо в файл
        filename = f"{ssid}.txt"
        content = f"WiFi: {ssid}\n"
        content += f"Password: {password}\n"
        content += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        content += "\n"
        content += "Usage:\n"
        content += f"1. Open WiFi settings\n"
        content += f"2. Find network: {ssid}\n"
        content += f"3. Enter password: {password}\n"
        content += "4. Connect\n"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✓ PASSWORD FOUND!")
        print(f"WiFi: {ssid}")
        print(f"Password: {password}")
        print(f"\nSaved to: {filename}")
    else:
        filename = f"{ssid}.txt"
        content = f"WiFi: {ssid}\n"
        content += f"Password: NOT FOUND\n"
        content += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        content += "\n"
        content += "This network was never connected before.\n"
        content += "Use: python wifi-brute-python.py -ssid \"{}\"\n".format(ssid)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✗ Password not found")
        print("This network was never connected before.")
        print(f"Use brute force: python wifi-brute-python.py -ssid \"{ssid}\"")
        print(f"\nInfo saved to: {filename}")

if __name__ == "__main__":
    main()

