import pandas as pd
# df = pd.read_csv("EQUITY_L.csv")
# df['Yahoo_Equivalent_Code'] = df['Yahoo_Equivalent_Code'].str.strip("',") 
# ans =df["Yahoo_Equivalent_Code"].tolist()


######################################################
#  got all the symols in nse                         #
###################################################### 
df= pd.read_excel("MCAP28032024.xlsx")
df['Symbol'] = df['Symbol'].astype(str) + '.NS'
all_nse_symbols=df["Symbol"].tolist()



# data = yf.download(ticker, start="2000-01-01", end="2024-01-03")