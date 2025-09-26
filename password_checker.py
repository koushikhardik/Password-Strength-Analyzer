import re

def assess_password_strength(password, common_passwords):
    """
    Analyzes the strength of a password based on several criteria.
    """
    feedback = []
    score = 0

    # 1. Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long (12+ is better).")

    # 2. Character Variety Check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'\d', password): # \d is for digits
        score += 1
    else:
        feedback.append("Add at least one number.")
        
    if re.search(r'[^A-Za-z0-9]', password): # Non-alphanumeric characters
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$%).")

    # 3. Common Password Check
    if password.lower() in common_passwords:
        score = 0 # Major penalty
        feedback.append("This is a very common password. Please choose something more unique.")

    # Final Rating
    if score >= 6:
        rating = "Very Strong"
    elif score >= 4:
        rating = "Strong"
    elif score >= 2:
        rating = "Medium"
    else:
        rating = "Weak"
        
    return rating, feedback

if __name__ == "__main__":
    try:
        with open('common_passwords.txt', 'r') as f:
            common_passwords = [line.strip().lower() for line in f]
    except FileNotFoundError:
        print("[WARN] common_passwords.txt not found. Running without checking for common passwords.")
        common_passwords = []

    print("--- Password Strength Analyzer ---")
    user_password = input("Enter a password to check: ")
    
    rating, feedback = assess_password_strength(user_password, common_passwords)
    
    print("\n--- Assessment ---")
    print(f"Password Rating: {rating}")
    
    if feedback:
        print("Suggestions for improvement:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Excellent password!")
