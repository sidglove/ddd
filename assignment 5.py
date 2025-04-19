o	# Program Name: Assignment5.py 
o	# Course: IT3883/Section 
o	# Student Name: Michael Glover
o	# Assignment Number: Lab 5
o	# Due Date: 04/18/2025
o	# Purpose: Make a data base for temperature readings




import sqlite3


    

def create_database(): 

    connection = sqlite3.connect('data_temperature.db')
    cur = connection.cursor()
    
    cur.execute('''
    CREATE TABLE Temperature (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT NOT NULL,
        Temperature_Value REAL NOT NULL
    )
''')
    connection.commit() 
    return connection     

def insert_sample_data(conn):
    cur = conn.cursor()  
    
    data_temperature = [
        ("Sunday", 72.5),
        ("Monday", 68.0),
        ("Tuesday", 70.2),
        ("Wednesday", 69.8),
        ("Thursday", 71.0),
        ("Friday", 67.5),
        ("Saturday", 73.3),
        ("Sunday", 74.2),
        ("Thursday", 70.1)
    ]

    for day, temp in data_temperature:
        cur.execute('''
            INSERT INTO Temperature (Day_Of_Week, Temperature_Value)
            VALUES (?, ?)
        ''', (day, temp))

    conn.commit()  
    return conn

def calculate_averages(connection):
    """Monday and Friday average calculated temperature printed."""
    cur = connection.cursor()
    
    
    cur.execute('''
        select AVG(Temperature_Value) 
        from Temperature 
        where Day_Of_Week = 'Monday'
    ''')
    Monday_avg = cur.fetchone()[0]
    
    
    cur.execute('''
        select AVG(Temperature_Value) 
        from Temperature 
        where Day_Of_Week = 'Friday'
''')
    Friday_avg = cur.fetchone()[0]
    
    print(f"Monday Average Temperature: {Monday_avg:.2f}°F")
    print(f"Friday Average Temperature: {Friday_avg:.2f}°F")

def main():
    """Main function"""
    try:
        
        connection = create_database()
        
      
        insert_sample_data(connection)
        
        
        calculate_averages(connection)
        
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    main()