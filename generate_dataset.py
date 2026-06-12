import pandas as pd
import numpy as np
from random import choice, randint, uniform

np.random.seed(42)

brands = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Hyundai", "Tata", "Mahindra"]
vehicle_types = ["Sedan", "SUV", "Hatchback", "Truck", "Van", "Coupe", "EV"]
fuel_types = ["Petrol", "Diesel", "Electric", "Hybrid"]
transmissions = ["Manual", "Automatic"]

rows = 70

data = {
    "Vehicle_ID": [f"V{1000+i}" for i in range(rows)],
    "Brand": [choice(brands) for _ in range(rows)],
    "Vehicle_Type": [choice(vehicle_types) for _ in range(rows)],
    "Year": [randint(2010, 2025) for _ in range(rows)],
    "Fuel_Type": [choice(fuel_types) for _ in range(rows)],
    "Transmission": [choice(transmissions) for _ in range(rows)],
}

# Add 64 more columns to reach 70 total
extra_columns = {
    "Engine_CC": np.random.randint(800, 5000, rows),
    "Cylinders": np.random.randint(2, 12, rows),
    "Horsepower": np.random.randint(60, 700, rows),
    "Torque_Nm": np.random.randint(80, 1000, rows),
    "Mileage_KMPL": np.round(np.random.uniform(8, 35, rows), 2),
    "Top_Speed": np.random.randint(120, 320, rows),
    "Acceleration_0_100": np.round(np.random.uniform(3, 18, rows), 2),
    "Fuel_Tank_Capacity": np.random.randint(30, 120, rows),
    "Length_mm": np.random.randint(3200, 5500, rows),
    "Width_mm": np.random.randint(1500, 2300, rows),
    "Height_mm": np.random.randint(1300, 2200, rows),
    "Wheelbase_mm": np.random.randint(2200, 3600, rows),
    "Ground_Clearance_mm": np.random.randint(120, 300, rows),
    "Kerb_Weight_kg": np.random.randint(800, 3500, rows),
    "Seating_Capacity": np.random.randint(2, 9, rows),
    "Airbags": np.random.randint(0, 10, rows),
    "ABS": np.random.randint(0, 2, rows),
    "ESP": np.random.randint(0, 2, rows),
    "Sunroof": np.random.randint(0, 2, rows),
    "Touchscreen_Size": np.round(np.random.uniform(5, 18, rows), 1),
    "Battery_Capacity_kWh": np.round(np.random.uniform(0, 120, rows), 1),
    "Charging_Time_Hours": np.round(np.random.uniform(0, 15, rows), 1),
    "Range_KM": np.random.randint(150, 800, rows),
    "Price_USD": np.random.randint(8000, 150000, rows),
    "Insurance_Cost": np.random.randint(300, 5000, rows),
    "Annual_Maintenance": np.random.randint(100, 4000, rows),
    "Resale_Value": np.random.randint(2000, 100000, rows),
    "Owner_Count": np.random.randint(1, 5, rows),
    "Service_Count": np.random.randint(0, 20, rows),
    "Warranty_Years": np.random.randint(0, 10, rows),
    "Crash_Rating": np.random.randint(1, 6, rows),
    "CO2_Emission": np.random.randint(0, 300, rows),
    "NOx_Emission": np.random.randint(0, 150, rows),
    "Tire_Size": np.random.randint(14, 24, rows),
    "Brake_Disc_Size": np.random.randint(200, 450, rows),
    "Drive_Type": np.random.randint(1, 4, rows),
    "Navigation_System": np.random.randint(0, 2, rows),
    "Bluetooth": np.random.randint(0, 2, rows),
    "Rear_Camera": np.random.randint(0, 2, rows),
    "Parking_Sensors": np.random.randint(0, 2, rows),
    "Cruise_Control": np.random.randint(0, 2, rows),
    "Lane_Assist": np.random.randint(0, 2, rows),
    "Adaptive_Cruise": np.random.randint(0, 2, rows),
    "Blind_Spot_Monitor": np.random.randint(0, 2, rows),
    "Autonomous_Level": np.random.randint(0, 5, rows),
    "City_Mileage": np.round(np.random.uniform(5, 25, rows), 2),
    "Highway_Mileage": np.round(np.random.uniform(8, 40, rows), 2),
    "Engine_Temperature": np.random.randint(70, 120, rows),
    "Oil_Consumption": np.round(np.random.uniform(0.1, 3.0, rows), 2),
    "RPM_Max": np.random.randint(4000, 9000, rows),
    "Gear_Count": np.random.randint(4, 10, rows),
    "Headlight_Type": np.random.randint(1, 4, rows),
    "Color_Code": np.random.randint(100, 999, rows),
    "Manufacturing_Plant": np.random.randint(1, 20, rows),
    "Sales_Last_Year": np.random.randint(100, 100000, rows),
    "Market_Share": np.round(np.random.uniform(0.1, 25, rows), 2),
    "Customer_Rating": np.round(np.random.uniform(1, 5, rows), 1),
    "Review_Count": np.random.randint(1, 5000, rows),
    "Recall_Count": np.random.randint(0, 10, rows),
    "Road_Tax": np.random.randint(100, 5000, rows),
    "Registration_Fee": np.random.randint(50, 2000, rows),
    "Import_Duty": np.random.randint(0, 15000, rows),
    "Luxury_Index": np.round(np.random.uniform(1, 10, rows), 1),
    "Performance_Index": np.round(np.random.uniform(1, 10, rows), 1),
}

data.update(extra_columns)

df = pd.DataFrame(data)

print("Columns:", len(df.columns))  # Should be 70
print("Rows:", len(df))             # Should be 70

df.to_csv("vehicles_70x70.csv", index=False)

print("vehicles_70x70.csv created successfully!")