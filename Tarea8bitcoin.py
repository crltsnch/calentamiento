bitcoin_amount = 1
bitcoin_value_euros = 25000

def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value

euros_value = bitcoinToEuros(bitcoin_amount, bitcoin_value_euros)

if euros_value <= 30000:
    print("Investment below 30000€! SELL!")
else:
    print("Investment above 30000€")

investment_in_bitcoin = 1.2
bitcoin_to_euros = 25000

def bitcoinToEuros (bitcoin_amount, bitcoin_value_euros):
    euro_value = bitcoin_amount * bitcoin_to_euros
    return(euro_value)

investment_in_euro = bitcoinToEuros(bitcoin_amount, bitcoin_value_euros)

if investment_in_euro <= 30000:
    print("Investment bellow 30000€! SELL")
else:
    print("Investment above 300000€")
    