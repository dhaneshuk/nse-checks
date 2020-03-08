import pandas as pd
import json
from nsetools import Nse

#
# Give your list of companies here
#
company_list = ['infy', 'icicibank', 'sbin', 'JUBILANT', 'CCL']
wanted_keys = ('bcEndDate', 'companyName', 'exDate', 'bcStartDate', 'dayHigh', 'basePrice', 'dayLow',
               'pChange', 'averagePrice', 'buyPrice1', 'high52', 'previousClose', 'low52', 'sellPrice1', 'isExDateFlag', 'closePrice'	'isinCode', 'lastPrice')
#
###########


nse = Nse()


def dictfilt(x, y): return dict([(i, x[i]) for i in x if i in set(y)])


list = []
for company in company_list:
    stock1 = nse.get_quote(company)
    stock = dictfilt(stock1, wanted_keys)
    list.append(stock)


df = pd.DataFrame(list)
# df.to_excel('stock_list.xlsx')
df.to_excel('stock_list.xlsx', startrow=1, sheet_name='Sheet1', index=False)
