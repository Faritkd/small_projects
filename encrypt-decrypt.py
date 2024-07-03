print("choose:\n 1. Encrypt\n 2.Decrypt\n 3.Exit")

choice = int(input("Your choice:"))

if choice == 1:
    text = input("Enter your text:")
    encrypted_text = ""
    for c in text:
        x = ord(c) * 5 + 3
        encrypted_text += chr(x)
    print(f"your encrypted text is '{encrypted_text}'")
    print("-" * 100)


if choice == 2: 
    encrypted_text = input("Enter your encrypted text:")
    text = ""
    for c in encrypted_text:
        x = (ord(c) - 3) // 5
        text += chr(x)
    print(f"your decrypted text is '{text}'")
    print("-"*100)


if choice == 3: 
    print("Auf Wiedersehen😘!")


else: 
    print("your choice is wrong. please choose between 1 to 3.")