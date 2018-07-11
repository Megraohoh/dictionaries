# Create a simple dictionary with ticker symbols and company names.
stock_dictionary = { 
    'AAT': 'American Assets Trust', 
    'ABR': 'Arbor Realty Trust Inc', 
    'ABX': 'Barrick Gold Corp'
    }

# Create a simple list of blocks of stock. (ticker, number of shares, purchased date, price)
purchases = [
    ('AAT', 100, '2-apr-1999', 48), 
    ('ABR', 101, '4-may-2000', 24), 
    ('ABX', 102, '5-jun-2000', 56)
    ]

# Create a purchase history report (full purchase price and full company name in output)
def purchase_history():
    print('Purchase History Report:')
    for purchase in purchases:
        if purchase[0] in stock_dictionary:
            print(f'{stock_dictionary[purchase[0]]} ({purchase[1] * purchase[3]})') 

purchase_history()

# Create a second purchase summary that which accumulates total investment by ticker symbol. 

# Steve's code:
portfolio = dict()
for purchase in purchases:
    ticker = purchase[0]

    full_company_name = stock_dictionary[ticker]
    number_of_shares = purchase[1]
    purchase_price = purchase[3]
    full_purchase_price = number_of_shares * purchase_price

    minimal_purchase = (purchase[1], purchase[2], purchase[3])

    try:
        # Append the purchase to the ticker list
        portfolio[ticker].append(purchase)
    except KeyError:
        portfolio[ticker] = list() #If the key doesn't exist yet, create it
        portfolio[ticker].append(purchase)

    print("I purchased {} stock for ${}".format(full_company_name, full_purchase_price))

    print(portfolio)

    for ticker, purchases in portfolio.items():
        print("------ {} ------".format(ticker))
        total_portfolio_stock_value = 0
        for purchase in purchases:
            total_portfolio_stock_value += purchase[1] * purchase[3]
            print("     {}".format(purchase))
        print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))