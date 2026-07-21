import random
import json
from datetime import datetime, timedelta

# Configuration
NUM_BATCHES = 100  # Each batch = 1000 records. Set to 10 for 10,000 records, etc.
RECORDS_PER_BATCH = 10000

# Sample datasets for realistic generation
LOCATIONS = [
    {"country": "India", "city": "Pune", "lat": (18.45, 18.65), "lon": (73.75, 73.95)},
    {"country": "India", "city": "Mumbai", "lat": (18.90, 19.25), "lon": (72.80, 73.00)},
    {"country": "India", "city": "Bengaluru", "lat": (12.85, 13.10), "lon": (77.50, 77.75)},
    {"country": "Germany", "city": "Munich", "lat": (48.10, 48.25), "lon": (11.50, 11.65)},
    {"country": "USA", "city": "Chicago", "lat": (41.75, 42.00), "lon": (-87.75, -87.55)},
]

VEHICLE_MODELS = {
    "Volvo": ["FH16", "FM", "FMX"],
    "Tata Motors": ["Prima", "Signa"],
    "Scania": ["R-Series", "S-Series"],
    "Daimler": ["Actros", "Atego"]
}

FAULT_CODES = ["", "", "", "", "P0300", "P0115", "P0500", "B0001"]  # Weighted towards empty
WEATHER_TYPES = ["Clear", "Rainy", "Cloudy", "Foggy"]

def generate_telemetry_record():
    loc = random.choice(LOCATIONS)
    manufacturer = random.choice(list(VEHICLE_MODELS.keys()))
    model = random.choice(VEHICLE_MODELS[manufacturer])
    
    engine_status = random.choice(["Running", "Idle", "Stopped"])
    
    # Dynamic values dependent on engine status
    if engine_status == "Stopped":
        speed = 0.0
        rpm = 0
        acceleration = 0.0
        oil_pressure = 0.0
        gear = 0
    elif engine_status == "Idle":
        speed = 0.0
        rpm = random.randint(600, 900)
        acceleration = 0.0
        oil_pressure = round(random.uniform(20.0, 35.0), 1)
        gear = 0
    else:  # Running
        speed = round(random.uniform(10.0, 110.0), 1)
        rpm = random.randint(1100, 2800)
        acceleration = round(random.uniform(-2.5, 3.0), 2)
        oil_pressure = round(random.uniform(45.0, 65.0), 1)
        gear = random.randint(1, 12)

    record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "vehicle_id": f"TRK_{random.randint(1, 999999):06d}",
        "fleet_id": f"{loc['country'].upper()}_{random.choice(['NORTH', 'SOUTH', 'EAST', 'WEST'])}_{random.randint(1, 99):02d}",
        "manufacturer": manufacturer,
        "vehicle_model": model,
        "driver_id": f"DRV_{random.randint(1, 999999):06d}",
        "country": loc["country"],
        "city": loc["city"],
        "latitude": round(random.uniform(*loc["lat"]), 5),
        "longitude": round(random.uniform(*loc["lon"]), 5),
        "speed": speed,
        "acceleration": acceleration,
        "heading": random.randint(0, 359),
        "engine_temperature": round(random.uniform(85.0, 105.0), 1),
        "coolant_temperature": round(random.uniform(75.0, 95.0), 1),
        "oil_pressure": oil_pressure,
        "engine_rpm": rpm,
        "gear_position": gear,
        "fuel_level": round(random.uniform(10.0, 100.0), 1),
        "fuel_consumption": round(random.uniform(18.0, 35.0), 1),
        "battery_voltage": round(random.uniform(11.8, 14.2), 1),
        "battery_efficiency": round(random.uniform(80.0, 99.0), 1),
        "tire_pressure": round(random.uniform(30.0, 36.0), 1),
        "odometer": round(random.uniform(10000.0, 500000.0), 1),
        "trip_distance": round(random.uniform(5.0, 800.0), 1),
        "brake_status": speed > 0 and random.choice([True, False, False]),
        "engine_status": engine_status,
        "fault_code": random.choice(FAULT_CODES),
        "signal_strength": random.randint(40, 100),
        "weather": random.choice(WEATHER_TYPES)
    }
    
    return record


# --- Example Usage ---
if __name__ == "__main__":
    # Generate records
    total_records = NUM_BATCHES * RECORDS_PER_BATCH
    records = [generate_telemetry_record() for _ in range(total_records)]
    
    # Save to JSON file
    output_file = f"data/telemetry_records_{total_records}.json"
    with open(output_file, "w") as f:
        json.dump(records, f, indent=2)
    
    print(f"Generated {total_records} records and saved to {output_file}")