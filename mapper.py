#!/usr/bin/env python
import sys

def main():
    next(sys.stdin)
    
    for line in sys.stdin:
        try:
            fields = line.strip().split(',')
            
            fuel_type = fields[6]   # 'Type of Fuel' column
            car_count = fields[8]   # 'CarCount' column
            
            # Emit (FuelType, CarCount)
            print(f"{fuel_type}\t{car_count}")
        except Exception as e:
            print(f"ERROR in mapper: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    main()