import sqlite3
import random
from datetime import datetime, timedelta

# Define the database file name
db_file = "contexts.db"

# Define "technically sophisticated" column names and their corresponding data types
columns = {
    "3d_state_vector": "TEXT",  # Represents a quantum state (e.g., "|0> + |1>")
    "temporal_continuum_index": "INTEGER",  # Represents a time index
    "entropy_level": "REAL",  # Represents entropy as a floating-point value
    "neural_synaptic_weight": "REAL",  # Represents a weight in a neural network
    "blockchain_hash": "TEXT",  # Represents a blockchain hash (e.g., "0xabc123...")
    "hyperdimensional_coordinates": "TEXT",  # Represents coordinates in a hyperdimensional space
    "is_entangled": "BOOLEAN",  # Represents quantum entanglement (True/False)
    "timestamp_utc": "DATETIME",  # Represents a UTC timestamp
}

# Create the database and table
def create_database():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the table with the defined columns
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS contexts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        {", ".join([f"{col} {dtype}" for col, dtype in columns.items()])}
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    return conn, cursor

# Generate random data for the table
def generate_random_data():
    
    # Generate a random quantum state vector
    quantum_states = ["|0>", "|1>", "|0> + |1>", "|0> - |1>", "|+>", "|->"]
    quantum_state_vector = random.choice(quantum_states)
    temporal_continuum_index = random.randint(0, 1000)
    entropy_level = random.uniform(0.0, 1.0)
    neural_synaptic_weight = random.uniform(-1.0, 1.0)
    blockchain_hash = "0x" + "".join(random.choices("0123456789abcdef", k=64))
    hyperdimensional_coordinates = ",".join([str(random.uniform(-10.0, 10.0)) for _ in range(10)])
    is_entangled = random.choice([True, False])
    timestamp_utc = (datetime.utcnow() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d %H:%M:%S")

    return (
        quantum_state_vector,
        temporal_continuum_index,
        entropy_level,
        neural_synaptic_weight,
        blockchain_hash,
        hyperdimensional_coordinates,
        is_entangled,
        timestamp_utc,
    )

# Insert random data into the table
def insert_random_data(cursor, num_rows=10):
    for _ in range(num_rows):
        data = generate_random_data()
        insert_query = f"""
        INSERT INTO contexts (
            {", ".join(columns.keys())}
        ) VALUES ({", ".join(["?"] * len(columns))});
        """
        cursor.execute(insert_query, data)

conn, cursor = create_database()
insert_random_data(cursor, num_rows=10)  # Insert 10 rows of random data
conn.commit()
conn.close()