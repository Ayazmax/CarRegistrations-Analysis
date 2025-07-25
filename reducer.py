#!/usr/bin/env python
import sys

def main():
    current_fuel = None
    total = 0
    
    for line in sys.stdin:
        try:
            fuel_type, count = line.strip().split('\t')
            count = int(count)
            
            if current_fuel == fuel_type:
                total += count
            else:
                if current_fuel:
                    print(f"{current_fuel}\t{total}")
                current_fuel = fuel_type
                total = count
                
        except ValueError:
            continue
    
    if current_fuel:
        print(f"{current_fuel}\t{total}")

if __name__ == "__main__":
    main()