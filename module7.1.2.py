from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


url = 'https://mfd.ru/currency/?currency=USD'
page = requests.get(url)
# check status
print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table',{'class':'mfd-table mfd-currency-table'})
rates = table.find_all('td')
rates = (i.text for i in rates)

lst = []
for i in rates:
    lst += str(i).split()


xvalue = [str(lst[i - 2]) for i in range(len(lst) -1, 3 , -4)]
yvalue = [float(str(lst[i-1])) for i in range(len(lst) -1, 3 , -4)]

figure, ax = plt.subplots()
ax.plot(xvalue, yvalue)
ax.xaxis.set_major_locator(MaxNLocator(5))
ax.grid(True)
ax.set(title='USD to RUB exchange rate')
ax.set(xlabel ='Date')
ax.set(ylabel ='Rate')
plt.show()


