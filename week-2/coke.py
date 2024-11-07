import sys

def main():
    accepted_coins = [1, 5, 10, 25]

    amount_due = 50
    print("Amount Due:", amount_due)

    coin = int(input("Insert Coin: "))

    while coin not in accepted_coins:
        print("Amount Due:", amount_due)
        coin = int(input("Insert Coin: "))
        continue

    while coin in accepted_coins:
        amount_due = amount_due - coin

        if amount_due > 0:
            coin = underpaid(amount_due, accepted_coins)
        elif amount_due < 0:
            overpaid(amount_due)
        elif amount_due == 0:
            print("Change Owed: 0")
            break


def underpaid(amount_due, accepted_coins):
    print("Amount Due:", amount_due)

    while True:
        coin = int(input("Insert Coin: "))

        if coin in accepted_coins:
            return coin


def overpaid(amount_due):
    print("Change Owed:", abs(amount_due))
    sys.exit()


main()