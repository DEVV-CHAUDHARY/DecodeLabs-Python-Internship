import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=" * 40)
    print("     RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    while True:
        try:
            length = int(input("\nEnter password length (minimum 4): "))

            if length < 4:
                print("❌ Password length should be at least 4.")
                continue

            password = generate_password(length)

            print("\n✅ Generated Password:")
            print(password)

            again = input("\nGenerate another password? (y/n): ").lower()

            if again != "y":
                print("\nThank you for using Password Generator.")
                break

        except ValueError:
            print("❌ Please enter a valid number.")


if __name__ == "__main__":
    main()