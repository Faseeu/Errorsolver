class KeyErrorHandler:
    def handle(self, error_message):
        print(f"Handling KeyError: {error_message}")
        # Improved suggestions for KeyError
        if "KeyError" in error_message:
            missing_key = error_message.split("'")[1]
            print(f"Suggestion: The key '{missing_key}' does not exist in the dictionary. Ensure the key is correct and exists in the dictionary.")
        else:
            print("Suggestion: Check your dictionary keys to make sure they are correct and exist before accessing them.")
