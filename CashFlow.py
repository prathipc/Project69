import pandas as pd
import requests
import json
#Its the same things.. Should I move it into an object class? May be... 

cf = requests.get('https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/AAPL?period=quarter')
cf = cf.json()

cash_flow = pd.DataFrame.from_dict(cf['financials'])
print ("Step 0.............")
print (cash_flow)

#Lets Transpose this as well...
cash_flow = cash_flow.T
print ("Step 1.............")
print (cash_flow)

cash_flow.columns = cash_flow.iloc[0]  
print ("Step 2.............")
print (cash_flow)

# Now delete the first row which is row 0... 
cash_flow = cash_flow.iloc[1:, ] # got rid of the first row.. 
print ("Step 3.............")
print (cash_flow)
print()
print()

# Now let us have only 4 quarters.. before that is all noise.. so let us delete them as well..... 
cash_flow = cash_flow.iloc[0: ,:4 ]
print ('step 4...............')
print (cash_flow)
print ()
print()

cols = cash_flow.columns
print (cols)
cash_flow[cols] = cash_flow[cols].apply(pd.to_numeric, errors = 'coerce')
pd.options.display.float_format = '{:.2f}'.format
print (cash_flow)
print (cash_flow.info())


