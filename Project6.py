import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''
    
    all_characters = lower + upper + digits + special
    
    if not all_characters:
        raise ValueError("At least one character type must be selected.")
    
    password = []
    
    if use_uppercase:
        password.append(random.choice(upper))
    if use_numbers:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))
        
    password += random.choices(all_characters, k=length - len(password))
    
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Password Generator")
    print("------------------")

    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()