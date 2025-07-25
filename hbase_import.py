#!/usr/bin/env python

import happybase

def connect_hbase():
    """Establish HBase connection"""
    return happybase.Connection('localhost')  # Use 'quickstart.cloudera' in VM

def import_data():
    conn = connect_hbase()
    table = conn.table('car_registrations')
    
    try:
        with open('fuel_analysis.txt', 'r') as f:
            for line in f:
                fuel_type, count = line.strip().split('\t')
                
                # Insert into HBase
                table.put(
                    fuel_type.encode('utf-8'),
                    {b'cf:count': count.encode('utf-8')}
                )
        print("Data imported successfully!")
    except Exception as e:
        print(f"Import failed: {str(e)}")

if __name__ == "__main__":
    import_data()