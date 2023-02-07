import pandas as pd

def get_interest(file):
    if(file.endswith('.csv')):
        df = pd.read_csv(open(file, 'r'), delimiter=';')
        
        stringval=""
        interest_list = df.values.tolist()
        for interest in interest_list:
            stringval+=str(interest[0])+","
        # print(stringval)
        return stringval
        # return df
    elif(file.endswith('.xlsx') or file.endswith('.xls')):
        df = pd.read_excel(file)
        stringval=""
        interest_list = df.values.tolist()
        for interest in interest_list:
            stringval+=str(interest[0])+","
        # print(stringval)
        return stringval
