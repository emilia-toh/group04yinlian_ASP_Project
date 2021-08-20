import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = pd.read_excel('IMVA.xls', sheet_name='IMVA')
print(file)

asia = file[['Periods', 'Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Thailand', 'Vietnam', 'China', 'Hong Kong SAR', 'Taiwan', 'Japan', 'South Korea', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Iran', 'Israel', 'Kuwait', 'Saudi Arabia', 'United Arab Emirates']]
print(asia.columns)
print(asia)

date = asia['Periods'].str.split(' ', n = 1, expand = True)
asia = asia.assign(year = date[0])
print(date)

asiayearsrange = asia[(asia['year'] >= str(2008)) & (asia['year'] <= str(2017))]
print(asiayearsrange)

#print(asia)
print(asiayearsrange.head(3))
print(asiayearsrange.tail(3))

asiadf = asiayearsrange[['Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Thailand', 'Vietnam', 'China', 'Hong Kong SAR', 'Taiwan', 'Japan', 'South Korea', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Iran', 'Israel', 'Kuwait', 'Saudi Arabia', 'United Arab Emirates']]
asiadf = asiadf.replace(',', '', regex=True)
asiadf = asiadf.replace('na', '0', regex=True)
print(asiadf)

asiadf = asiadf.astype(int)
calculate = asiadf.sum()
print(calculate)
sort = calculate.sort_values(ascending=False)
print(sort)

sorttop3 = sort.head(3)
print(sorttop3)

class Calculate:
    def sum(num):
        return sum(num)

    def mean(num):
        return sum(num)/len(num)

print("The total no. of visitors for the top 3 countries is" , Calculate.sum(sorttop3))
print("The mean value for the top 3 countries is", round(Calculate.mean(sorttop3), 2))

ps = sorttop3.sort_values(ascending=False)
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=10)
plt.ylabel('No. of Travellers(in thousands)', fontsize=10)
plt.xticks(index, ps.index, fontsize=10, rotation=45)
plt.title('Top 3 Asia Countries from (Periods: 2008 - 2017)')
plt.bar(ps.index, ps.values/1000)
plt.show()

ps = calculate.sort_values(ascending=False)
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=10)
plt.ylabel('No. of Travellers(in thousands)', fontsize=10)
plt.xticks(index, ps.index, fontsize=10, rotation=45)
plt.title('Top 3 Asia Countries from (Periods: 2008 - 2017)')
plt.bar(ps.index, ps.values/1000)
plt.show()

