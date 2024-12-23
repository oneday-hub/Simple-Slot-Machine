import random

def print_slot(slot):
    """Prints the slot rows in a readable format."""
    for row in slot:
        print(" | ".join(row))

def spin_slot_machine(rows, cols, symbols):
    """Generates the slot machine grid based on given symbols."""
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)
    
    slot = []
    for _ in range(rows):
        row = random.sample(all_symbols, cols)
        slot.append(row)
    return slot

def check_winnings(slot, bet, lines, symbols):
    """Calculates winnings based on matching lines."""
    winnings = 0
    for line in range(lines):
        if len(set(slot[line])) == 1:  # All symbols in the line are the same
            winnings += bet * symbols[slot[line][0]]
    return winnings

def main():
    # Symbols and their values
    symbols = {"A": 10, "B": 8, "C": 6, "D": 4}
    symbol_count = {"A": 3, "B": 4, "C": 5, "D": 6}

    print("Welcome to the Slot Machine!")
    
    # Number of rows and columns in the slot machine
    rows, cols = 3, 3

    balance = 100  # Initial player balance
    while balance > 0:
        print(f"\nCurrent Balance: ${balance}")
        bet = int(input("Enter your bet (or 0 to quit): "))
        if bet == 0 or bet > balance:
            print("Exiting the game. Goodbye!")
            break

        lines = int(input(f"Enter the number of lines to bet on (1-{rows}): "))
        if lines < 1 or lines > rows:
            print("Invalid number of lines.")
            continue
        
        print("\nSpinning the slot machine...\n")
        slot = spin_slot_machine(rows, cols, symbol_count)
        print_slot(slot)

        winnings = check_winnings(slot, bet, lines, symbols)
        balance += winnings - (bet * lines)
        print(f"\nYou won ${winnings}!")
        if winnings > 0:
            print("Congratulations!\n")
        else:
            print("Better luck next time.\n")
        
    print("\nYou have no money left. Thanks for playing!")

if __name__ == "__main__":
    main()
