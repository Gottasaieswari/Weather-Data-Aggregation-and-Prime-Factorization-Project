Here’s a complete `README.md` file for your project:

---

## **Weather Data Aggregation and Prime Factorization Project**

### **Description:**

This project contains two main tasks:

1. **Weather Data Aggregation**: A Python function that processes a list of city weather records, calculating the average temperature and humidity for each city. The function handles missing data gracefully.
  
2. **Prime Factorization**: A Python function that performs prime factorization on a given integer, returning a list of prime factors along with their exponents.

3. **SQL Price Update**: An SQL query that increases the price of all products in a `products` table by 10%, and displays the updated product prices along with their names.

---

### **Project Structure:**

```
assignment/
│
├── weather_and_prime.py        # Python file for weather data aggregation and prime factorization
├── update_product_prices.sql   # SQL file to increase product prices by 10%
└── README.md                   # Instructions for running the project
```

---

### **Prerequisites:**

- **Python 3.x** should be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **SQL Database Setup**: You should have access to a database management tool such as MySQL Workbench or pgAdmin, or you can use an SQL extension in VS Code.
  
---

### **How to Run the Python Script:**

1. Open your terminal or command line.

2. Navigate to the project folder:
   
   ```bash
   cd path/to/weather_prime_project
   ```

3. Run the Python script by executing the following command:

   ```bash
   python weather_and_prime.py
   ```

4. The script will print:
   - The aggregated weather data (average temperature and humidity) for each city.
   - The prime factorization of a sample integer (e.g., 60).

#### **Example Output:**

For weather data aggregation:

```bash
Aggregated Weather Data: {
    'CityA': {'average_temperature': 22.5, 'average_humidity': 30.0},
    'CityB': {'average_temperature': 22.0, 'average_humidity': 52.5}
}
```

For prime factorization of 60:

```bash
Prime Factorization of 60: [(2, 2), (3, 1), (5, 1)]
```

---

### **How to Run the SQL Query:**

1. Open your preferred SQL client (e.g., MySQL Workbench, pgAdmin) or use an SQL extension in VS Code.

2. Load the `update_product_prices.sql` file.

3. Run the following SQL query to:
   - Increase the price of all products by 10%.
   - Display the updated prices along with product names.

#### **SQL Query Content:**

```sql
-- Increase the price of all products by 10%
UPDATE products
SET price = price * 1.10;

-- Display the new prices with product names
SELECT name, price
FROM products;
```

4. Once executed, the query will update the prices and return the new prices for all products.

---

### **Conclusion:**

This project demonstrates how to process weather data and perform prime factorization using Python, as well as how to manipulate data using SQL queries. Follow the instructions above to run the Python script and SQL queries.