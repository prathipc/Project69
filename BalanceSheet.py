import pandas as pd
import requests
import json
bs = requests.get('https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/AAPL?period=quarter')
bs = bs.json()

balance_sheet = pd.DataFrame.from_dict(bs['financials'])
print ("Step 0.............")

print (balance_sheet)

balance_sheet = balance_sheet.T # to transpose the balance sheet... :-) cool shit...!
print ("Step 1.............")
print (balance_sheet)
print()
print()

# Here when we transposed in the previous step - The older index 0, 1, 2, 3 became the columns. So we have to get rid of it..  
# to do that .. let us copy the row 1 to row 0... 
balance_sheet.columns = balance_sheet.iloc[0]  
print ("Step 2.............")
print (balance_sheet)
print()
print()

# Now delete the first row which is row 0... 
balance_sheet = balance_sheet.iloc[1:, ] # got rid of the first row.. 
print ("Step 3.............")
print (balance_sheet)
print()
print()

# Now let us have only 4 quarters.. before that is all noise.. so let us delete them as well..... 
balance_sheet = balance_sheet.iloc[0: ,:4 ]

print ('step 4...............')
print (balance_sheet)
print ()
print()

cols = balance_sheet.columns
print (cols)
balance_sheet[cols] = balance_sheet[cols].apply(pd.to_numeric, errors = 'coerce')
print (balance_sheet)
print (balance_sheet.info())

# Split the balance sheet into Assets, Equity and Liablities... 
assets = balance_sheet.iloc[:12,]

print ('step 5 --- Assests only')
print (assets)
print (assets.info())

#Spliit the equity portion 
lb_eq = balance_sheet.iloc[13:,]

print ('step 6 --- Liablity & equity only')
print (lb_eq)

# Now calculate some metrics on the assets we have... 
assetCol = cols = assets.columns
assetsQ1 = assets.iloc[11,0]
assetsQ2 = assets.iloc[11,1]
assetsQ3 = assets.iloc[11,2]
assetsQ4 = assets.iloc[11,3]
allassets = [assetsQ1,assetsQ2,assetsQ3,assetsQ4]
assets[assetCol] = (assets[assetCol] / allassets)*100

#pd.options.display.float_format = ‘{:.2f}%’.format
pd.options.display.float_format = '{:.2f}%'.format
#Final Step
print (assets)
