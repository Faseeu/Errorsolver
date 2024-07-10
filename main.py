import capture.capture_errors as capture_errors
import analysis.analyze_errors as analyze_errors
import suggestions.suggest_solutions as suggest_solutions
import vscode_interaction.interact_vscode as interact_vscode
import ui.display_ui as display_ui

def main():
    # Initialize the UI
    ui = display_ui.UI()

    # Initialize the error analyzer
    error_analyzer = analyze_errors.ErrorAnalyzer()
    
    # Initialize the suggestion module
    solution_suggester = suggest_solutions.SolutionSuggester()
    
    # Initialize the VS Code interaction module
    vscode_interactor = interact_vscode.VSCodeInteractor()

    # Set up observers for the error capture module
    error_capture = capture_errors.ErrorCapture()
    error_capture.attach_observer(error_analyzer)
    error_capture.attach_observer(solution_suggester)
    error_capture.attach_observer(ui)

    # Start capturing errors
    error_capture.start_capture()

    # Start the UI
    ui.run()

if __name__ == "__main__":
    main()
