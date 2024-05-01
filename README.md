# BLE Bulb MITM
This repo contains the work i have done to make a script that performs an attack similar to what gattacker does.
The file ble_scan.py scans for nearby ble devices(in this case, a ble bulb) and stores its MAC address, its name and its rssi to a text file.
After the MAC address has been obtained, run the save-chara.py, where it will ask you the MAC address of the BLE device. Once you've provided the MAC addresss, the script will then attempt to make a connection with the BLE device and extract all of its services and characteristics, and saves it to a JSON file.

# Spoofing the peripheral
spoofing the peripheral does not work entirely for some reason. I spent a lot of time trying to get bluez to advertise the GATT profile, but the services and characteristics i defined were not showing up in a BLE exploration tool(nRF Connect). The device name would show up, but the services and characteristics were not showing up the way I defined it to. At one point, I tried to use Bleno to emulate the peripheral device, but could not get it to work. To install it, I had to downgrade NodeJS to v8.9.0, and the installation was done. I tried writing a test script by just importing Bleno, but when i tried to run it, it said that the bluetooth-hci-socket was missing, so i tried to install that. That's when more errors in installation came. Tried googling the error codes, and found out that it could be fixed by using @abandonware/node-bluetooth-hci-socket. I replaced it in the Packages.JSON file, but for some reason, i could not execute my test code. I'm still working on it by trying different tools to do this.

# BLE Bulb Colour Changing
this can be done by running the ble-colour-change.py, where it will connect to the BLE bulb, and it will ask you for the RGBW values. Input the values and the color will change to what was entered.
