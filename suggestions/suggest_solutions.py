import re

class SolutionSuggester:
    def update(self, error_message):
        self.suggest_solution(error_message)

    def extract_error_location(self, error_message):
        match = re.search(r'File "(.+)", line (\d+)', error_message)
        if match:
            return match.group(1), match.group(2)
        return None, None

    def suggest_solution(self, error_message):
        file, line = self.extract_error_location(error_message)
        location_info = f"Error in file: {file}, line: {line}" if file and line else "Error location not found"
        print(location_info)
        
        if "SyntaxError" in error_message:
            self.suggest_syntax_fix(error_message, location_info)
        elif "ImportError" in error_message:
            self.suggest_import_fix(error_message, location_info)
        elif "TypeError" in error_message:
            self.suggest_type_fix(error_message, location_info)
        elif "NameError" in error_message:
            self.suggest_name_fix(error_message, location_info)
        elif "IndexError" in error_message:
            self.suggest_index_fix(error_message, location_info)
        elif "KeyError" in error_message:
            self.suggest_key_fix(error_message, location_info)
        else:
            print(f"Suggestion: No specific solution available for the error: {error_message}")

    def suggest_syntax_fix(self, error_message, location_info):
        print(f"Solution Suggestion for SyntaxError at {location_info}:")
        print("1. Review the line indicated in the error message.")
        print("2. Ensure all parentheses, brackets, and colons are correctly placed and matching.")
        print("3. Check for any missing punctuation or incorrect indentation.")
        print("4. Example: If you have an 'if' statement, ensure it ends with a colon (:).")

    def suggest_import_fix(self, error_message, location_info):
        print(f"Solution Suggestion for ImportError at {location_info}:")
        print("1. The module mentioned in the error may not be installed or is misspelled.")
        print("2. Ensure the module name is correct and installed.")
        print("3. Install the missing module using 'pip install module_name'.")
        print("4. Example: If the error is 'No module named requests', install it using 'pip install requests'.")

    def suggest_type_fix(self, error_message, location_info):
        print(f"Solution Suggestion for TypeError at {location_info}:")
        print("1. Check the types of variables and values being used in the operation.")
        print("2. Ensure that you're not mixing incompatible types, such as adding a string to a number.")
        print("3. Convert values to the correct type using functions like str(), int(), or float() as needed.")
        print("4. Example: If you have '3' + 3, convert the number to a string: '3' + str(3).")

    def suggest_name_fix(self, error_message, location_info):
        print(f"Solution Suggestion for NameError at {location_info}:")
        print("1. The variable or function name mentioned in the error is not defined.")
        print("2. Ensure the name is spelled correctly and is defined before it's used.")
        print("3. Check for typos and make sure the definition is in the correct scope.")
        print("4. Example: If you have 'print(my_var)' and 'my_var' is not defined, define it first: 'my_var = 10'.")

    def suggest_index_fix(self, error_message, location_info):
        print(f"Solution Suggestion for IndexError at {location_info}:")
        print("1. The index you're trying to access is out of range.")
        print("2. Ensure the index is within the bounds of the list or array.")
        print("3. Check the length of the list or array and use valid indices.")
        print("4. Example: If you have 'my_list[5]' and 'my_list' has only 3 elements, use a valid index like 'my_list[2]'.")

    def suggest_key_fix(self, error_message, location_info):
        print(f"Solution Suggestion for KeyError at {location_info}:")
        print("1. The key mentioned in the error does not exist in the dictionary.")
        print("2. Ensure the key is correct and exists in the dictionary before accessing it.")
        print("3. Use dictionary methods like get() to safely access keys.")
        print("4. Example: If you have 'my_dict['missing_key']', use 'my_dict.get('missing_key', default_value)' to avoid errors.")
