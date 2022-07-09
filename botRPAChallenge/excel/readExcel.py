import pandas as pd

datatable = pd.read_excel(r"C:\Projetos\RPAChalenge\botRPAChallenge\excel\challenge.xlsx")

#print(datatable)

for index,row in datatable.iterrows():
    first_name =  row[0]
    last_name =  row[1]
    company = row[2]
    role = row[3]
    address =  row[4]
    email = row[5]
    phone = row[6]

    print(first_name,last_name,company,role,address,email,phone)

    
