import pandas as pd

#all_data = pd.read_csv("globalterroris.csv", encoding = "ISO-8859-1");

#relevant_data =  all_data[['eventid','iyear', 'country_txt', 'latitude', 'longitude', 'nkill']]
#print(relevant_data)
#relevant_data.to_csv("relevant_terrorist.csv",index=False)

relevant_data = pd.read_csv("relevant_terrorist.csv", encoding = "ISO-8859-1");

#print(relevant_data.groupby(['country_txt','iyear']).size())
i = relevant_data[['country_txt', 'nkill', 'longitude', 'latitude', 'iyear']]
i.dropna(inplace=True)
d1 = i.groupby(['iyear']).size()
#print(i.count())
#print(d1)
print(d1.idxmax())
print(d1.max())
#print(d1.mean())

d3 = i[['iyear', 'nkill']]
d3 = d3.dropna()

print(d3)
print(d3['nkill'].mean())

d3 = d3.groupby(['iyear']).size()
print(d3.mean())

d4 = i[['iyear', 'nkill']]
d4 = d4.dropna()

d4 = d4.groupby(['iyear']).sum()
print(d4.mean())

d = i[['country_txt', 'nkill']]
#d = d.dropna()
print((d.groupby(['country_txt']).sum()).max())
print((d.groupby(['country_txt']).sum()).idxmax())

#print(relevant_data[relevant_data['nkill'] > 1200])

d = i[['country_txt']]
print(d.groupby(['country_txt']).size().max())
#print(d.idxmax())
