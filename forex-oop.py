from urllib.request import urlopen
import json
from secrets import *
import pandas as pd
import numpy as np
apikey = "M0E2RAZRGG836JDA"

def show_c():
    #list_c = pd.read_csv('list.csv')
    print("@@Enter the currency/country name@@")
    name = input().upper()
    a = pd.read_csv('list.csv')
    a['Currency'] = a['Currency'].str.upper()
    b = a['Currency'].str.contains(name)
    x = b[b==True]
    x = x.index
    if len(x) == 0:
        print("Please enter a valid name, Try again")
        show_c()
    else:
        print(a['Currency'][x] +" " + a['Alphabetic_Code'][x])  
    
    
def get_rate(fc,tc):
    #print("Enter three letter currency code, Press 1 if you want to lookup symbol ")
    if fc == "":
        fc = "USD"
    #fc = input()
    """try:
        if int(fc) == 1:
            show_c()
            fc = input("Enter FROM Currency\n")
    except ValueError:
        pass"""

    """if fc == "":
        print("No FROM currency entered default is USD")
        fc = "USD"""

    #tc = input("Enter TO currency \n")
    """while tc=="":
        tc = input("TO currency cannot be empty !!!\n")"""
    """fc = fc.upper()
    fc = fc.strip()
    tc = tc.upper()
    tc = tc.strip()"""

    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" +fc+"&to_currency="+tc+"&apikey="+apikey

    try:
        response = urlopen(url)
        data = json.loads(response.read())
            try:
                a_d = dict(data["Realtime Currency Exchange Rate"])
                a = pd.DataFrame(data = a_d, index = [0])
                #print("From"+"\t"+fc+" To"+"\t"+tc+"\nThe Exchange Rate is \t"+a["5. Exchange Rate"][0])
                #print("One "+fc+" = "+a['5. Exchange Rate'][0] +" "+ tc)
                return a['5. Exchange Rate'][0]
            except KeyError:
                err = "Please Enter Valid Details"
                return err
    except urllib.error.URLError:
        err = "Please Ensure an active internet connection"
        return err

   
"""if __name__=='__main__':
    get_rate()"""