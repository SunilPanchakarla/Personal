import pandas as pd
df = pd.DataFrame(
    [("01/01/2023",	100	,"Credit",	1000),
    ("01/02/2023",	100	,"Credit",	1500),
    ("01/03/2023",	100	,"Debit",	1000),
    ("01/02/2023",	200	,"Credit",	3500),
    ("01/03/2023",	200	,"Debit",	2000),
    ("01/04/2023",	200	,"Credit",	3500),
    ("01/13/2023",	300	,"Credit",	4000),
    ("01/14/2023",	300	,"Debit",	4500),
    ("01/15/2023",	300	,"Credit",	1500)])

df.columns =['Transaction_Date', 'Account_Number', 'Transaction_Type', 'Amount']

df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date']).dt.strftime('%m-%d-%Y')

df.loc[df['Transaction_Type'] == "Debit",'Amount'] *= -1
df.sort_values(['Account_Number','Transaction_Date'], ascending=[True,True],inplace=True)

df['Current_Balance'] = df.groupby(['Account_Number'])['Amount'].cumsum()
print(df)



