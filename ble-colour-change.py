import asyncio 
from bleak import BleakClient
async def main():
    address = "F8:1D:78:63:17:63"
    service_uuid = "0000FFE5-0000-1000-8000-00805F9B34FB"
    char_uuid = "0000FFE9-0000-1000-8000-00805F9B34FB"
#bruh main
    async with BleakClient(address) as client:
        print(f"Connected: {await client.is_connected()}")

        while True:
            val1 = input("Enter RGBW values(RRGGBBWW): ")
            val="56"+val1+"f0aa"
            try:
                val = bytes.fromhex(val)
            except ValueError:
                print("Invalid input. Please enter a valid hexadecimal value.")
                continue
            await client.write_gatt_char(char_uuid, val, response=True)
            print("Value written to the characteristic.")
            continue_input = input("Do you want to continue? (yes(y)/no(n)): ")
            if continue_input.lower() not in ["yes",'y']:
                break

asyncio.run(main())