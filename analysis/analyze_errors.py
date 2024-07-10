import re
from handlers.syntax_error_handler import SyntaxErrorHandler
from handlers.import_error_handler import ImportErrorHandler
from handlers.type_error_handler import TypeErrorHandler
from handlers.name_error_handler import NameErrorHandler
from handlers.index_error_handler import IndexErrorHandler
from handlers.key_error_handler import KeyErrorHandler

class ErrorAnalyzer:
    def __init__(self):
        # Initialize handlers for different types of errors
        self.handlers = {
            "SyntaxError": SyntaxErrorHandler(),
            "ImportError": ImportErrorHandler(),
            "TypeError": TypeErrorHandler(),
            "NameError": NameErrorHandler(),
            "IndexError": IndexErrorHandler(),
            "KeyError": KeyErrorHandler(),
            # Add more handlers here
        }

    def update(self, error_message):
        self.analyze_error(error_message)

    def analyze_error(self, error_message):
        for error_type, handler in self.handlers.items():
            if error_type in error_message:
                handler.handle(error_message)
                break
        else:
            print(f"Unrecognized error: {error_message}")
