import pyautogui
import time

def record_positions():
    """
    Prompts the user to record mouse positions.
    Returns a list of (x, y) positions.
    """
    positions = []
    num_positions = int(input("How many positions do you want to record? "))

    for i in range(num_positions):
        input(f"Move your mouse to position #{i+1} and press ENTER to record...")
        x, y = pyautogui.position()
        positions.append((x, y))
        print(f"Position #{i+1} recorded at ({x}, {y})")

    print("\nRecording completed.")
    print("Positions recorded:", positions)
    return positions

def automate_clicks(positions, delay=1.0, iterations=100):
    """
    Loops through the recorded positions and automates clicks.

    Parameters:
      positions - List of (x, y) positions to click.
      delay - Time delay (in seconds) after each click.
      iterations - Number of times to loop through the positions.
    """
    print("\nAutomation will start in 3 seconds. Press Ctrl+C to abort if necessary...")
    time.sleep(3)  # Countdown before automation starts

    for i in range(iterations):
        print(f"\n--- Iteration {i + 1} of {iterations} ---")
        for idx, (x, y) in enumerate(positions, start=1):
            # Move the mouse to the position with a smooth movement
            pyautogui.moveTo(x, y, duration=0.5)
            # Click at the position
            pyautogui.click()
            print(f"Clicked position #{idx} at ({x}, {y})")
            # Wait for the specified delay before moving to the next position
            time.sleep(delay)

    print("\nAutomation complete!")

if __name__ == "__main__":
    print("=== Mouse Position Recorder and Click Automator ===")
    
    # Step 1: Record positions
    recorded_positions = record_positions()
    
    # Prompt the user to specify how many times the automation should run
    iterations = int(input("Enter the number of times you want to run the automation: "))
    
    # Step 2: Automate clicks with user-specified iterations
    automate_clicks(recorded_positions, delay=1.0, iterations=iterations)
