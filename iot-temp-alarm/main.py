import random
import time

# Simulated temperature sensor function
def read_temperature():
    return round(random.uniform(20.0, 40.0), 2)

# Threshold
THRESHOLD = 30.0

def check_temperature():
    temp = read_temperature()
    print(f"Temperature: {temp}°C")
    if temp > THRESHOLD:
        print("⚠️ ALERT: High temperature detected!")
    else:
        print("✅ Temperature is normal.")

if __name__ == "__main__":
    print("Starting simulated temperature monitor...")
    for _ in range(5):
        check_temperature()
        time.sleep(2)
