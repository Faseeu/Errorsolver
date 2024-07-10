class ImportErrorHandler:
    def handle(self, error_message):
        print(f"Handling ImportError: {error_message}")
        # Improved suggestions for ImportError
        if "No module named" in error_message:
            missing_module = error_message.split("named")[-1].strip()
            print(f"Suggestion: The module '{missing_module}' is not installed or misspelled. Use 'pip install {missing_module}' to install it or check for typos.")
        else:
            print("Suggestion: Ensure all modules you're trying to import are correctly installed and named.")
