# Python-Mouse-Click-Automation-Script

## Overview

This Python-based tool automates repetitive mouse click tasks by recording specific positions on your screen and simulating mouse clicks at those positions. You can customize both the number of positions recorded and the number of iterations for the automation process, along with setting a delay between each click.

## Features

- **Record Mouse Positions:**  
  Record custom mouse positions by manually positioning your mouse and pressing Enter.

- **Automated Mouse Clicks:**  
  Uses the [pyautogui](https://pypi.org/project/pyautogui/) library to simulate mouse movement and clicks at the recorded positions.

- **Configurable Iterations:**  
  Prompts you to specify how many times you want the automation to run, instead of using a fixed default value.

- **Delay Customization:**  
  A delay is applied between clicks to ensure smooth and controlled automation.

## Requirements

- **Python 3.x**
- **pyautogui Library**  
  Install using pip:
  ```bash
  pip install pyautogui
  ```

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/mouse-click-automation.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd mouse-click-automation
   ```
3. **Install Dependencies:**  
   Ensure you have installed the required dependencies (e.g., `pyautogui`) as mentioned in the [Requirements](#requirements) section.

## Usage

1. **Run the Script:**
   ```bash
   python automation.py
   ```
2. **Record Positions:**  
   - The script will prompt you to enter the number of positions you want to record.
   - For each position, move your mouse to the desired location and press Enter. The (x, y) coordinates will be recorded and displayed.
3. **Set Automation Iterations:**  
   - After recording the positions, the script will prompt you to enter the number of iterations (i.e., how many times you want the automation to run).
4. **Automation Process:**  
   - A 3-second countdown is provided before the automation begins.
   - The script will loop through all recorded positions for the specified number of iterations.
   - At each position, the mouse will move (with a smooth transition) and click, then wait for the set delay (default 1 second) before proceeding.
5. **Abort Operation:**  
   - If necessary, press `Ctrl+C` in the terminal to stop the script during automation.

## Example Workflow

1. Run the script with `python automation.py`.
2. Enter the number of positions to record (e.g., 3).
3. Move your mouse to each desired position and press Enter to record each position.
4. Enter the number of iterations you want the automation to run (e.g., 100).
5. The script will start the automation after a brief countdown, clicking at each recorded position in sequence for the specified number of iterations.

## Important Notes

- **Testing:**  
  Always test the script in a controlled environment to ensure it behaves as expected.

- **Permissions:**  
  On some systems (like macOS), you may need to enable accessibility or screen recording permissions for your Python interpreter or terminal application.

- **Usage Caution:**  
  Use the script carefully to avoid unintended actions. Ensure you have a method to regain control (e.g., using `Ctrl+C` to abort the process).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pyautogui](https://pypi.org/project/pyautogui/) for providing an easy way to automate GUI interactions.
- The open-source community for continuous support and contributions.

