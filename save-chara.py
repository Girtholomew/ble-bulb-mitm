import asyncio
from bleak import BleakClient, BleakScanner
import json

async def save_services_and_characteristics(mac_address):
    # Find the device by its MAC address
    device = await BleakScanner.find_device_by_address(mac_address)
    
    async with BleakClient(device) as client:
        print(f"Connected: {await client.is_connected()}")
        
        # Prepare the data structure to save
        data = {"device_name": device.name, "services": []}
        
        # Iterate through services and prepare the data
        for service in client.services:
            service_data = {"uuid": service.uuid, "description": service.description, "characteristics": []}
            for char in service.characteristics:
                char_data = {"uuid": char.uuid, "description": char.description}
                service_data["characteristics"].append(char_data)
            data["services"].append(service_data)
        
        # Save the data to a JSON file
        with open('advertisements.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("Data saved to advertisements.json")

async def main():
    # Ask the user for the MAC address of the BLE device
    mac_address = input("Enter the MAC address of the BLE device: ")
    
    # Connect to the BLE device and save its services and characteristics
    await save_services_and_characteristics(mac_address)

if __name__ == "__main__":
    asyncio.run(main())
