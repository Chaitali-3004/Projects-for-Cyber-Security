
import re
import sys

def check_password_strength(password):
    """Evaluates password strength based on different criteria."""
    
    strength = 0
    feedback = []

    # Checking password length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("🔹 Password should be at least 8 characters long.")

    # Checking for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("🔹 Include at least one uppercase letter (A-Z).")

    # Checking for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("🔹 Include at least one lowercase letter (a-z).")

    # Checking for numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("🔹 Include at least one digit (0-9).")

    # Checking for special characters
    if re.search(r"[!@#$%^&*()_+=\[\]{};:'\",.<>?/\\|`~]", password):
        strength += 1
    else:
        feedback.append("🔹 Include at least one special character such as (!@#$%^&* etc.).")

    # Password strength message
    if strength == 5:
        print("\n✅ Your password is **Strong**! 💪")
    elif strength >= 3:
        print("\n⚠️ Your password is **Moderate**. Consider making it stronger.")
    else:
        print("\n❌ Your password is **Weak**. Please improve it!")

    # Show improvement suggestions
    if feedback:
        print("\nSuggestions to improve your password:")
        for tip in feedback:
            print(tip)

def ask_user():
    """Asks the user if they want to check another password."""
    while True:
        choice = input("\nDo you want to check another password? (y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            sys.exit("\n👋 Exiting... Stay secure!")
        else:
            print("❌ Invalid input! Please enter 'y' or 'n'.")

# Main execution
if __name__ == "__main__":
    print("🔒 **Welcome to the Password Strength Checker!** 🔒\n")

    while True:
        password = input("Enter a password to check its strength: ")
        check_password_strength(password)
        
        # Ask if they want to check another password
        if not ask_user():
            break
