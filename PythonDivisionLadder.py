import os
import time

def run_ladder(n):
    temp_n = n
    factors = []
    
    # Division by 2
    while temp_n % 2 == 0:
        divisor = 2
        factors.append(divisor)
        print(f"{divisor:^10} | {temp_n:^10}")
        print("-----------|-----------") # Added line
        temp_n //= divisor
        
    # Division by odd numbers
    f = 3
    while f * f <= temp_n:
        while temp_n % f == 0:
            factors.append(f)
            print(f"{f:^10} | {temp_n:^10}")
            print("-----------|-----------") # Added line
            temp_n //= f
        f += 2
        
    # Final prime factor
    if temp_n > 1:
        factors.append(temp_n)
        print(f"{temp_n:^10} | {temp_n:^10}")
        print("-----------|-----------") # Added line
        temp_n //= temp_n 
        
    # Show the final "1" at the bottom
    print(f"{'':^10} | {1:^10}")
        
    return factors

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    user_input = input("\nEnter number: ")
    os.system('cls' if os.name == 'nt' else 'clear')
        
    try:
        num = int(user_input)
        if num < 2:
            input("Use a number > 1. Press Enter...")
            continue
            
        res = run_ladder(num)
        print("-----------|----------- \n")
        print(f"     {' × '.join(map(str, res))}")
        input("\nPress Enter for next number...")
        
    except ValueError:
        input("Invalid input! Press Enter...")
