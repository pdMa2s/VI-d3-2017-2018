import pandas as pd

all_data = pd.read_csv("globalterroris.csv", encoding = "ISO-8859-1");

relevant_data =  all_data[['eventid','iyear', 'country_txt', 'latitude', 'longitude', 'nkill']]
print(relevant_data)
relevant_data.to_csv("relevant_terrorist.csv",index=False)
