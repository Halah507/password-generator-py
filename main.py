import csv
import random
import string
import os

def generate_password(length):
    letters = string.ascii_letters     
    digits = string.digits             
    symbols = string.punctuation        
    all_chars = letters + digits + symbols

    return ''.join(random.choices(all_chars, k=length))

def save_password(service, password):
    file_exist = os.path.isfile("passwords.csv")

    with open('passwords.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exist or os.path.getsize("passwords.csv") == 0:
            writer.writerow(['Service', 'Password'])
        writer.writerow([service, password])

def main():
    service = input("What service is this password for?: ").strip()
    
    while True:
        try:
            length = int(input("How long should the password be?: ").strip())
            if length < 1:
                print("⚠ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("⚠ Please enter a valid number.")
    
    password = generate_password(length)
    print(f"Your generated password: {password}")
    save_password(service, password)
    print("✅ Your password info has been saved to the CSV file.")

if __name__ == "__main__":
    main()