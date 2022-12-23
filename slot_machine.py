import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWs = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


#def check_winnings(columns,lines,bet,values):
#    winnings = 0
#    winnings_lines = []
#    for line in range(lines):
#        symbol = columns[0][line]
#        for column in columns:
#            symbol_to_check = column[line]
#            if symbol != symbol_to_check:
#                break
#        else:
#            winnings += values[symbol] * bet
#            winnings_lines.append(line + 1)
#
#    return winnings, winnings_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    colums = [[],[],[]]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            Value = random.choice(current_symbols)
            current_symbols.remove(Value)
            column.append(Value)

        colums.append(column)
    
    return colums

def print_slot_machines(colums):
    for row in range(len(colums[0])):
        for i, column in enumerate(colums) :
           if i != len(colums) - 1 : 
            print(column[row], end=" | ")
           else:
            print(column[row], end="")
        print() 

def deposit():
    while True:
        amount = input("what would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amount must be greater than 0 ")
        else:
            print("pleaase enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
        
    return lines

def get_bet():
    while True:
        amount = input("what would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between $`^{MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number")
        
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"you do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break 

    print(f"you are betting ${bet} on {lines} lines. Total bet is equal ${total_bet}")

    slot = get_slot_machine_spin(ROWs,COLS,symbol_count)
    print(slot)
    winnings, winning_lines = check_winnings(slot,lines,bet,symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on", *winning_lines)
main()
