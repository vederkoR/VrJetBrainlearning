# Write your code here
import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
)
;''')
conn.commit()
conn.close()


class BankAccount:
    def __init__(self, card_number=None, pin='0000', balance=0):
        self.balance = balance
        self.card_number = card_number
        self.pin = pin

    def generate_nuber(self):
        account_part = str(random.randint(0, 9_999_999_99))
        card_number_wo_last = '400000' + (9 - len(account_part)) * '0' + account_part
        self.card_number = card_number_wo_last + BankAccount.luhn_generate(card_number_wo_last)

    def generate_pin(self):
        gen_pin = str(random.randint(0, 9999))
        self.pin = (4 - len(gen_pin)) * '0' + gen_pin

    @staticmethod
    def luhn_generate(n):
        step_1_n = [int(i) for i in n]
        step_2_n = []
        for inx, elem in enumerate(step_1_n):
            if inx % 2 == 1:
                step_2_n.append(elem)
            else:
                step_2_n.append(elem * 2)
        step_3_n = [i if i < 10 else i - 9 for i in step_2_n]
        step_4_n = str(1000 - sum(step_3_n))
        return step_4_n[-1]


bank_accounts = dict()


def add_to_database(account):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute(f'''INSERT INTO card (number, pin)
    VALUES ({account.card_number}, {account.pin})
    ''')
    conn.commit()
    conn.close()


def load_databases():
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute(f'''SELECT *
    FROM card    
    ''')
    entry = cur.fetchone()
    while entry:
        account_to_load = BankAccount(card_number=entry[1], pin=entry[2], balance=entry[3])
        bank_accounts[account_to_load.card_number] = account_to_load
        entry = cur.fetchone()
    conn.close()


def check_input(i):
    return int(i) in range(3)


def main():
    load_databases()
    print(BankAccount.luhn_generate('400000712807361'))
    while True:
        print("1. Create an account\n2. Log into account\n0. Exit")
        checked = input()
        if not check_input(checked):
            print("\nThis option doesn't exist\n")
            continue
        if checked == '1':
            new_account = BankAccount()
            new_account.generate_nuber()
            new_account.generate_pin()
            add_to_database(new_account)
            bank_accounts[new_account.card_number] = new_account
            print("\nYour card has been created")
            print(f"Your card number:\n{new_account.card_number}")
            print(f"Your card PIN:\n{new_account.pin}\n")

        elif checked == '2':
            print("\nEnter your card number:")
            card_number = input()
            account = bank_accounts.get(card_number, None)
            print("Enter your PIN:")
            pin = input()
            if account:
                if pin != account.pin:
                    print("\nWrong card number or PIN!\n")
                else:
                    print("\nYou have successfully logged in!\n")
                    while True:
                        print("1. Balance\n2. Log out\n0. Exit")
                        checked_2 = input()
                        if not check_input(checked_2):
                            print("\nThis option doesn't exist\n")
                            continue
                        if checked_2 == '1':
                            print(f'Balance: {account.balance}\n')
                        elif checked_2 == '2':
                            break
                        else:
                            print('\nBye!')
                            return
            else:
                print("\nWrong card number or PIN!\n")
        else:
            print('Bye!')
            return


if __name__ == '__main__':
    main()

