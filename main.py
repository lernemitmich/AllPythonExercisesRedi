def check_palindrome(word):
    reversed_word = word[::-1]  # Reverse the word
    
    if word == reversed_word:
        return True  # Word is a palindrome
    else:
        return False  # Word is not a palindrome

def run_palindrome_checker():
    print("Welcome to the Palindrome Checker App!")
    print("Enter 'exit' to quit the app.")

    while True:
        word = input("\nEnter a word: ")
        
        if word.lower() == 'exit':
            print("Thank you for using the Palindrome Checker App. Goodbye!")
            break
        
        if len(word) % 2 != 0:
            print("The word should have an even number of letters.")
            continue
        
        is_palindrome = check_palindrome(word)
        
        if is_palindrome:
            print(f"Yes, '{word}' is a palindrome!")
        else:
            print(f"No, '{word}' is not a palindrome.")

# Run the app
run_palindrome_checker()