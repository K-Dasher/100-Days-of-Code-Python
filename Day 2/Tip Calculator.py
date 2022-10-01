def main():
    print("Welcome to the Tip Calculator.")
    _totalAmount = float(input("What was the total bill? ₹"))
    print(f"Total Amount entered = ₹{_totalAmount}")
    _tipPercent = float(input("What percentage of tip would you like to give? "))
    print(f"{_tipPercent}% tip is to be given.")
    _totalPeople = int(input("How many people to split the bill?"))
    print(f"The bill should be split equally between {_totalPeople} people.")
    _perPersonAmt = _totalAmount*(1+(_tipPercent/100))/_totalPeople
    print(f"Each person should pay ₹{_perPersonAmt}")

if __name__ == "__main__":
    main()