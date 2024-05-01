# BLE Bulb MITM
This repo contains the work i have done to make a script that performs an attack similar to what gattacker does.
The file ble_scan.py scans for nearby ble devices(in this case, a ble bulb) and stores its MAC address, its name and its rssi to a text file.
After the MAC address has been obtained, run the save-chara.py, where it will ask you the MAC address of the BLE device. Once you've provided the MAC addresss, the script will then attempt to make a connection with the BLE device and extract all of its services and characteristics, and saves it to a JSON file.

# Spoofing the peripheral
