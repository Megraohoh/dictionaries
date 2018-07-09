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