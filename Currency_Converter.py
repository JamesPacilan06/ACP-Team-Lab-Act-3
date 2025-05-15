from abc import ABC, abstractmethod

class Currency(ABC):
    def __init__(self, currency_name, symbol, exchange_rate_to_usd):
        self.currency_name = currency_name
        self.symbol = symbol
        self.exchange_rate_to_usd = exchange_rate_to_usd

    @abstractmethod
    def convert_to(self, other_currency, amount):
        pass

class USD(Currency):
    def __init__(self):
        super().__init__("US Dollar", "$", 1.0)
    
    def convert_to(self, other_currency, amount):
        usd_amount = amount * self.exchange_rate_to_usd
        converted_amount = usd_amount / other_currency.exchange_rate_to_usd
        return converted_amount

class Yen(Currency):
    def __init__(self):
        super().__init__("Japanese Yen", "¥", 0.007)

    def convert_to(self, other_currency, amount):
        usd_amount = amount * self.exchange_rate_to_usd
        converted_amount = usd_amount / other_currency.exchange_rate_to_usd
        return converted_amount

class Euro(Currency):
    def __init__(self):
        super().__init__("Euro", "€", 1.123)
        
    def convert_to(self, other_currency, amount):
        usd_amount = amount * self.exchange_rate_to_usd
        converted_amount = usd_amount / other_currency.exchange_rate_to_usd
        return converted_amount
    
class Php(Currency):
    def __init__(self):
        super().__init__("Philippine Peso", "₱", 0.018)

    def convert_to(self, other_currency, amount):
        usd_amount = amount * self.exchange_rate_to_usd
        converted_amount = usd_amount / other_currency.exchange_rate_to_usd
        return converted_amount
    
class KRW(Currency):
    def __init__(self):
        super().__init__("Korean Won", "₩", 0.001)

    def convert_to(self, other_currency, amount):
        usd_amount = amount * self.exchange_rate_to_usd
        converted_amount = usd_amount / other_currency.exchange_rate_to_usd
        return converted_amount


def main():

    currencies = {
        "1": USD(),
        "2": Yen(),
        "3": Euro(),
        "4": Php(),
        "5": KRW()
                 }

    while True:

        print("\n=======================================")
        print("      MEOWMEOWPUSA CURRENCY CONVERTER    ")
        print("=======================================")

        print("\nCurrencies available:")
        for key, currency in currencies.items():
            print(f"{key}. {currency.currency_name}")

        convert_from = input("Choose a Currency to Convert From: ").strip()
        convert_to = input("Choose a Currency to Convert To: ").strip()

        if convert_from not in currencies or convert_to not in currencies:
            print("Invalid Currrency. Please choose from the currencies available.")
            continue
        
        convert_from_currency = currencies[convert_from]
        convert_to_currency = currencies[convert_to]
        
        try:
           amount = float(input(f"Enter amount in {convert_from_currency.currency_name}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        converted_amount = convert_from_currency.convert_to(convert_to_currency, amount)

        print(f"\n{convert_from_currency.symbol}{amount:,.2f} {convert_from_currency.currency_name} = " 
              f"{convert_to_currency.symbol}{converted_amount:,.2f} {convert_to_currency.currency_name}")

        choice = input("\nWould you like to convert again? (Y/N): ").strip().upper()
        if choice == 'N':
            print("Thank you for using currency converter!")
            break
        if choice == 'Y':
            continue
        else:
            print("Please choose Y/N only.")

main()