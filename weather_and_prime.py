# weather_and_prime.py

# Task 1: Aggregating Weather Data
def aggregate_weather_data(records):
    """
    Aggregates weather data for each city, calculating the average temperature
    and humidity while handling missing data gracefully.

    Args:
    records (list): A list of dictionaries where each dictionary contains the
                    city name and weather data (temperature, humidity).

    Returns:
    dict: A dictionary where each city is associated with its average
          temperature and humidity.
    """
    city_data = {}

    # Step 1: Collect data for each city
    for record in records:
        city = record.get("city")  # Safely get the city name
        if city not in city_data:
            # Initialize temperature and humidity lists for each city
            city_data[city] = {"temperature": [], "humidity": []}
        
        # Add temperature to the city's data if present
        if "temperature" in record:
            city_data[city]["temperature"].append(record["temperature"])
        
        # Add humidity to the city's data if present
        if "humidity" in record:
            city_data[city]["humidity"].append(record["humidity"])
    
    # Step 2: Calculate the average temperature and humidity for each city
    result = {}
    for city, data in city_data.items():
        # Calculate average temperature if data exists, otherwise None
        avg_temp = sum(data["temperature"]) / len(data["temperature"]) if data["temperature"] else None
        # Calculate average humidity if data exists, otherwise None
        avg_humidity = sum(data["humidity"]) / len(data["humidity"]) if data["humidity"] else None
        # Store the results for each city
        result[city] = {"average_temperature": avg_temp, "average_humidity": avg_humidity}
    
    return result

# Task 2: Prime Factorization
def prime_factorization(n):
    """
    Performs prime factorization of a given integer n and returns the prime factors
    along with their exponents.

    Args:
    n (int): The integer to factorize.

    Returns:
    list: A list of tuples where each tuple contains a prime factor and its exponent.
    """
    i = 2  # Start with the smallest prime number
    factors = []
    
    # Step 1: Find prime factors by dividing n by increasing i values
    while i * i <= n:  # Only check up to the square root of n
        count = 0
        while (n % i) == 0:  # While i divides n, divide n by i
            n //= i
            count += 1  # Keep track of the exponent
        if count > 0:
            factors.append((i, count))  # Append the prime factor and its exponent
        i += 1

    # Step 2: If there is a remaining prime factor greater than 1
    if n > 1:
        factors.append((n, 1))  # n itself is a prime factor
    
    return factors

# Example usage for Task 1: Weather Data Aggregation
weather_records = [
    {"city": "CityA", "temperature": 20, "humidity": 30},
    {"city": "CityA", "temperature": 25},  # Missing humidity
    {"city": "CityB", "humidity": 50},  # Missing temperature
    {"city": "CityB", "temperature": 22, "humidity": 55},
    {"city": "CityC"}  # Missing both temperature and humidity
]

print("Aggregated Weather Data:", aggregate_weather_data(weather_records))

# Example usage for Task 2: Prime Factorization
n = 60
print("Prime Factorization of 60:", prime_factorization(n))

# Additional tests for Task 2
n = 100
print("Prime Factorization of 100:", prime_factorization(n))

n = 37  # Prime number
print("Prime Factorization of 37:", prime_factorization(n))
