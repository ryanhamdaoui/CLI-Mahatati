import requests
import sys
from datetime import datetime, timedelta

def format_date(date_obj):
    return date_obj.strftime("%d%m%Y")

def format_time(time_str):
    try:

        time_obj = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S")

        return time_obj.strftime("%I:%M %p")
    except ValueError:
        return "N/A"

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <departure_zip_code> <destination_zip_code>")
        sys.exit(1)


    departure_middle = sys.argv[1].zfill(2)
    destination_middle = sys.argv[2].zfill(2)

    departure = f"213-0000{departure_middle}"
    destination = f"213-0000{destination_middle}"


    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    dates = [format_date(today), format_date(tomorrow)]


    headers = {
        "Host": "mahatati.sogral.com",
        "Accept-Encoding": "gzip, deflate, br"
    }

    all_buses = []

    for date in dates:
        url = f"https://mahatati.sogral.com/api/live/departures/search?Departure={departure}&Destination={destination}&Date={date}"
        print(f"\n🔍 Fetching buses for {date}...")
        try:
            response = requests.get(url, headers=headers)
            buses = response.json()
            if buses:
                for bus in buses:
                    bus["__date"] = date  
                    all_buses.append(bus)
        except Exception as e:
            print(f"Error fetching buses for {date}: {e}")

    if not all_buses:
        print("\nNo buses found for today or tomorrow.")
        return


    all_buses.sort(key=lambda b: b.get("P2", ""))


    print("\n🚌 Combined Bus Results:\n" + "-" * 40)
    for i, bus in enumerate(all_buses, start=1):
        time = format_time(bus.get("P2", "N/A"))
        license_plate = bus.get("P23", "N/A")
        bus_name = bus.get("P10", "N/A")
        route = bus.get("S6", "N/A")
        price = bus.get("S15", 0) + bus.get("S18", 0)
        bus_date = datetime.strptime(bus["__date"], "%d%m%Y").strftime("%A, %d %B %Y")
        departure = bus.get("S4", "N/A")
        destination = bus.get("S12", "N/A")
        print(f"Bus {i}:")
        print(f"  Date          : {bus_date}")
        print(f"  Time          : {time}")
        print(f"  License Plate : {license_plate}")
        print(f"  Bus Name      : {bus_name}")
        print(f"  Route         : {route}")
        print(f"  Departure     : {departure}")
        print(f"  Destination   : {destination}")
        print(f"  Price         : {price} DZD")
        print("-" * 40)

if __name__ == "__main__":
    main()
