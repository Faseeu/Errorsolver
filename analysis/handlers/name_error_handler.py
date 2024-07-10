class NameErrorHandler:
    def handle(self, error_message):
        print(f"Handling NameError: {error_message}")
        # Improved suggestions for NameError
        if "name" in error_message and "is not defined" in error_message:
            missing_name = error_message.split("'")[1]
            print(f"Suggestion: The name '{missing_name}' is not defined. Make sure it's spelled correctly and declared before use.")
        else:
            print("Suggestion: Check for typos in variable or function names and ensure they are defined before use.")
