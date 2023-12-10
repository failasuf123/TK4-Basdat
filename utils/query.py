import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    # connection = psycopg2.connect(user="postgres",
    #                               password="AeE1f32gg1db5-222ef5BA2F2*eGfD64",
    #                               host="monorail.proxy.rlwy.net",
    #                               port="40602",
    #                               database="railway")

    connection = psycopg2.connect(user="postgres",
                                  password="tk4basdatkelompok",
                                  host="db.lwwncffkfxoaqkovrloj.supabase.co",
                                  port="5432",
                                  database="postgres")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
    
    # Test
    cursor.execute(f"""
     SELECT R.hotel_name,R.price, R.floor, HF.facility_name
    FROM ROOM R
    JOIN HOTEL H ON R.hotel_name = H.hotel_name AND R.hotel_branch = H.hotel_branch
    JOIN hotel_facilities HF ON HF.hotel_name = H.hotel_name AND HF.hotel_branch = H.hotel_branch;
    """)
    record = cursor.fetchall()
    print(record)
    for n in record:
        print(n[0])

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)