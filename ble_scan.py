import asyncio
from bleak import BleakScanner

async def scan_and_save():
  devices = await BleakScanner.discover()
  with open("advertisement.txt", 'w') as file:
    for d in devices:
      if 'LED' in d.name:
        print("BLE Led lamp found!\nData saved to advertisement.txt")
        address = d.address
        name = d.name
        rssi = d.rssi
        file.write(f"Address: {address}\n")
        file.write(f"Name: {name}\n")
        file.write(f"RSSI: {rssi} dBm\n")
loop = asyncio.get_event_loop()
loop.run_until_complete(scan_and_save())