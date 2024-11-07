import sys

def main():
    accepted_coins = [1, 5, 10, 25]
    amount_due = 50

    print("Amount Due:", amount_due)

    coin = get_valid_coin(accepted_coins)
    
    while True:
        amount_due -= coin

        if amount_due > 0:
            coin = get_valid_coin(accepted_coins)
        elif amount_due < 0:
            handle_overpaid(abs(amount_due))
        else:
            print("Change Owed: 0")
            break

def get_valid_coin(accepted_coins):
    while True:
        coin = int(input("Insert Coin: "))

        if coin in accepted_coins:
            return coin

def handle_overpaid(change_owed):
    print("Change Owed:", change_owed)
    sys.exit()

main()
