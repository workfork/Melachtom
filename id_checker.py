def stat(id_number):
    # Convert incoming integer to string and pad with leading zeros to 9 digits
    id_number_str = str(id_number).zfill(9)
    
    # Check if the format is correct (9 digits)
    if not id_number_str.isdigit() or len(id_number_str) != 9:
        print("Invalid format")
        return False
    
    sum_total = 0
    for i, char in enumerate(id_number_str):
        digit = int(char)
        factor = 1 if i % 2 == 0 else 2
        product = digit * factor
        if product > 9:
            product -= 9
        sum_total += product
    
    if sum_total % 10 == 0:
        print("Valid ID")
        return True
    else:
        print("Invalid ID")
        return False

# Allow running from CLI
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python id_checker.py <id_number>")
        sys.exit(1)
    result = stat(sys.argv[1])
    print(result)
