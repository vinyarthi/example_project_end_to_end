from __future__ import annotations

from core.calculator import add, divide, multiply, subtract

OPS = {"+": add, "*": multiply, "/": divide, "-": subtract}


def parse_input_numbers(input_str: str) -> tuple[float, float]:
    parts = input_str.strip().split()
    if len(parts) != 2:
        raise ValueError(
            "Please enter exactly two numbers separated by space. Example: '12 43'"
        )
    return (float(parts[0]), float(parts[1]))


def main() -> None:
    print("Calculator CLI")
    print("Available operations: +, -, *, /, clear, exit")
    print("Usage: choose an operation, then enter two numbers like: '12 43'")

    while True:
        user_input = input("op> ").strip().lower()

        if user_input in ("exit", "quit", "q"):
            print("Bye.")
            return

        if user_input in ("clear", "cls", "c"):
            print("Cleared.\n")
            continue

        if user_input not in OPS:
            print("Invalid operation. Please enter a valid operation (+, -, *, /).")
            continue

        try:
            num1, num2 = parse_input_numbers(input("nums> "))
            operation = OPS[user_input]
            result = operation(num1, num2)
            print(f"Result: {result}\n")
        except ValueError as ve:
            print(f"Input error: {ve}\n")
        except ZeroDivisionError as zde:
            print(f"Math error: {zde}\n")


if __name__ == "__main__":
    main()
