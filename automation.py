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
        print(f"✔ Position #{i+1} recorded at ({x}, {y})")

    print("\n✅ All positions recorded successfully.")
    print("📍 Positions recorded:", positions)
    return positions

def automate_clicks(positions, delay=1.0, iterations=1):
    """
    Automates clicking through recorded positions.
    
    Parameters:
      - positions: List of (x, y) positions to click.
      - delay: Time delay (in seconds) between clicks.
      - iterations: Number of times to loop through positions.
    """
    print("\n⏳ Automation will start in 3 seconds. Press Ctrl+C to abort if needed...")
    time.sleep(3)  # Countdown before automation begins

    for i in range(iterations):
        print(f"\n🔄 Iteration {i + 1} of {iterations}")
        for idx, (x, y) in enumerate(positions, start=1):
            # Move mouse smoothly and click
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
            print(f"🖱 Clicked position #{idx} at ({x}, {y})")
            time.sleep(delay)  # Wait for the next click

    print("\n✅ Automation completed successfully!")

if __name__ == "__main__":
    print("🎯 Welcome to Mouse Click Automation 🎯\n")
    
    # Step 1: Record positions
    recorded_positions = record_positions()
    
    # Step 2: Set number of iterations
    iterations = int(input("🔄 Enter the number of times you want to run the automation: "))

    # Step 3: Automate clicks
    automate_clicks(recorded_positions, delay=1.0, iterations=iterations)
