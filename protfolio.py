
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 120,
    "MSFT": 310
}

portfolio = {}
while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

total_investment = 0
print("\nYour Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares x ₹{price} = ₹{value}")

print(f"\nTotal Investment: ₹{total_investment}")


save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            f.write(f"{stock},{quantity},{price},{value}\n")
        f.write(f"\nTotal Investment:,₹{total_investment}")
    print(f"Portfolio saved to {filename}")
