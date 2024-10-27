# Truman Forey | 9/23/2024 | Module 8 Assignment

# This program is an experiment with python dictionaries, using
# stock tickers as a key and their current price as a value.
# This program uses fake stock data for sake of experimentation.
# This program also returns an error if the user enters a ticker
# that is not in the dictionary.

stock_prices = {
  "MXJ": 103.91,
  "WAAS": 51.06,
  "GS": 29.25,
  "WONY": 66.80,
  "NPN" : 45.03,
  "AARD": 9.54,
  "JJJ": 0.51,
  "ZSP": 290.18,
  "UUR": 139.92,
  "WEST": 172.06
}

print("The current stock tickers listed are:")
print("MXJ, WAAS, GS, WONY, NPN, AARD, JJJ, ZSP, UUR, WEST")

def stock_check():
  user_input = input("Please enter the stock ticker you would like to see the price of: >")
  print("")
  # added an upper function to make sure the user input matches case of dictionary
  user_input = user_input.upper()
  if user_input in stock_prices:
    print("The current price of " + user_input + " is $" + str(stock_prices[user_input]) + ".")
  else:
    print("That stock ticker is not in our database. Please try again.")
  print("")
  stock_check()

stock_check()



