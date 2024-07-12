from rich.console import Console
from rich.text import Text
import random

class BeautifyOutput:
    def __init__(self):
        self.console = Console()
        self.COLORS = {
            "red": "#F28FAD",  # Cappuccin
            "green": "#ABE9B3",  # Cappuccin
            "yellow": "#FAE3B0",  # Cappuccin
            "blue": "#96CDFB",  # Cappuccin
            "magenta": "#DDB6F2",  # Cappuccin
            "cyan": "#89DCEB",  # Cappuccin
            "white": "#D9E0EE",  # Cappuccin
            "vibrancy_red": "#FF5555",  # Vibrancy Continued
            "vibrancy_green": "#50FA7B",  # Vibrancy Continued
            "vibrancy_yellow": "#F1FA8C",  # Vibrancy Continued
            "vibrancy_blue": "#BD93F9",  # Vibrancy Continued
            "vibrancy_magenta": "#FF79C6",  # Vibrancy Continued
            "vibrancy_cyan": "#8BE9FD",  # Vibrancy Continued
            "vibrancy_white": "#F8F8F2",  # Vibrancy Continued
            "vibrancy_black": "#282A36"  # Vibrancy Continued
        }
        self.error_color = self.COLORS['red']

    def display_error(self, error_message):
        text = Text(error_message, style=f"bold {self.error_color}")
        self.console.print(text)

    def display_suggestion(self, suggestion):
        suggestion_colors = [color for name, color in self.COLORS.items() if color != self.error_color]
        random_color = random.choice(suggestion_colors)
        text = Text(suggestion, style=f"bold {random_color}")
        self.console.print(text)
