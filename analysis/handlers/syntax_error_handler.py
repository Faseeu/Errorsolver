class SyntaxErrorHandler:
    def handle(self, error_message):
        print(f"Handling SyntaxError: {error_message}")
        # Improved suggestions for SyntaxError
        if "unexpected EOF while parsing" in error_message:
            print("Suggestion: You might be missing a closing parenthesis, bracket, or colon. Double-check the syntax.")
        elif "invalid syntax" in error_message:
            print("Suggestion: There's a syntax error in your code. Look for missing punctuation or incorrect indentation near the error location.")
        else:
            print("Suggestion: Review the code near the error location for any syntax mistakes.")
