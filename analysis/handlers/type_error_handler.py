class TypeErrorHandler:
    def handle(self, error_message):
        print(f"Handling TypeError: {error_message}")
        # Improved suggestions for TypeError
        if "unsupported operand type(s)" in error_message:
            print("Suggestion: You're using the wrong type of data in an operation. Check if you're mixing incompatible types, like adding a string to a number.")
        elif "must be str, not" in error_message:
            print("Suggestion: You're trying to use a non-string value where a string is expected. Convert your value to a string with str().")
        else:
            print("Suggestion: Review your function parameters and variable assignments to ensure the data types are correct.")
