import time
from pynput.keyboard import Controller, Key

keyboard = Controller()

def auto_typer(text, delay, repetitions):

    print("Starting the auto typer. Press Ctrl+C to stop.")
    print("You Have 10 seconds, GO GO GO GO GO!!!")
    time.sleep(10)

    for i in range(repetitions):
        for char in text:
            keyboard.type(char)
            time.sleep(delay)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        print(f"Typed: ({i + 1}/{repetitions})")
        time.sleep(delay)

if __name__ == "__main__":
    message = str(input("Enter the message you want to type: "))
    interval = float(input("Enter the interval between each character (in seconds): "))
    repeat = int(input("Enter the number of times you want to repeat the message: "))

    try:
        auto_typer(message, interval, repeat)
        print("Auto typer completed. Have a nice day!")

    except KeyboardInterrupt:
        print("\nAuto typer stopped.")
