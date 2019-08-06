from urllib.request import urlopen
import urllib
import json
from secrets import *
import pandas as pd
import numpy as np

def show_c():
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
    if fc == "":
        fc = "USD"

    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" +fc+"&to_currency="+tc+"&apikey="+apikey

    try:
        response = urlopen(url)
        data = json.loads(response.read())
        try:
            a_d = dict(data["Realtime Currency Exchange Rate"])
            a = pd.DataFrame(data = a_d, index = [0])
            return a['5. Exchange Rate'][0]
        except KeyError:
            err = "Please Enter Valid Details"
            return err
    except urllib.error.URLError:
        err = "Please Ensure an active internet connection"
        return err