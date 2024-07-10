class IndexErrorHandler:
    def handle(self, error_message):
        print(f"Handling IndexError: {error_message}")
        # Improved suggestions for IndexError
        if "list index out of range" in error_message:
            print("Suggestion: You're trying to access an index that doesn't exist. Ensure the index is within the range of the list or array.")
        else:
            print("Suggestion: Review the indices used in your list or array operations to ensure they are valid.")
