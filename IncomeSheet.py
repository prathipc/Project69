import pandas as pd
import requests
import json
incSheet = requests.get('https://financialmodelingprep.com/api/v3/financials/income-statement/MAC?period=quarter')
incSheet = incSheet.json()

income_sheet = pd.DataFrame.from_dict(incSheet['financials'])
print ("Step 0.............")
print (income_sheet)

#Lets Transpose this as well...
income_sheet = income_sheet.T

print ("Step 1.............")
print (income_sheet)

income_sheet.columns = income_sheet.iloc[0]  
print ("Step 2.............")
print (income_sheet)

# Now delete the first row which is row 0... 
income_sheet = income_sheet.iloc[1:, ] # got rid of the first row.. 
print ("Step 3.............")
print (income_sheet)
print()
print()



# Now let us have only 4 quarters.. before that is all noise.. so let us delete them as well..... 
income_sheet = income_sheet.iloc[0: ,:4 ]

print ('step 4...............')
print (income_sheet)
print ()
print()

cols = income_sheet.columns
print (cols)
income_sheet[cols] = income_sheet[cols].apply(pd.to_numeric, errors = 'coerce')

pd.options.display.float_format = '{:.2f}'.format

print (income_sheet)
print (income_sheet.info())


