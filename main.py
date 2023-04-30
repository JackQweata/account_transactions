from src.operation import AccountTransactions
from utils.receiving_invoices import get_invoice


def main():
    list_operations = get_invoice()

    for items in list_operations:
        account = AccountTransactions(items)

        print(f"{account.get_date()} "
              f"{account.get_description()}\n{account.get_from_operation()} -> "
              f"{account.get_to_operation()}\n{account.get_amount()}\n")


if __name__ == '__main__':
    main()
