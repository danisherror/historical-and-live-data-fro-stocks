import pandas as pd
import yfinance as yf
import logging
from datetime import datetime, timedelta
import json


#######################################################################################
#                                    Get historical data                              #
#   Date          Open         High          Low        Close    Adj Close     Volume #
#                                                                                     #
# [                                                                                   #
#     {'Date': '2024-08-16',                       {date }                            #
#     'Open': 2937.3,                         {float}                                 #
#     'High': 2960.8,                          {float}                                #
#     'Low': 2916.1,                            {float}                               #
#     'Close': 2956.4,                          {float}                               #
#     'Adj Close': 2956.4,                     {float}                                #
#     'Volume': 4708451                         {int}                                 #
#     }                                                                               #
# ]                                                                                   #
#######################################################################################
# file_path = 'symbols_results.xlsx'
# invalid_df = pd.read_excel(file_path, sheet_name='Valid Symbols')["Valid Symbols"].tolist()
# for ticker in invalid_df:
#     data = yf.download(ticker, start="1950-01-01", end=None)
#     df = pd.DataFrame(data)
#     formatted_data = [
#     {
#         "Date": date.strftime('%Y-%m-%d'),
#         "Open": round(float(row["Open"]), 3),
#         "High": round(float(row["High"]), 3),
#         "Low": round(float(row["Low"]), 3),
#         "Close": round(float(row["Close"]), 3),
#         "Adj Close": round(float(row["Adj Close"]), 3),
#         "Volume": int(row["Volume"])
#     }
#     for date, row in df.iterrows()
#     ]
#     beautified_json = json.dumps(formatted_data, indent=4)
#     with open('data.txt', 'w') as f:
#         f.write(f"{beautified_json}\n")
#     break
######################################################################################




#######################################################################################
#         Get historical data  for last month with 5 min interval                     #
#   Date          Open         High          Low        Close    Adj Close     Volume #
#                                                                                     #
# [                                                                                   #
#     {'Date': '2024-08-16',                       {date }  %Y-%m-%d'                 #
#     "Time": "09:15:00",                           {time}  '%H:%M:%S')               #
#     'Open': 2937.3,                         {float}                                 #
#     'High': 2960.8,                          {float}                                #
#     'Low': 2916.1,                            {float}                               #
#     'Close': 2956.4,                          {float}                               #
#     'Adj Close': 2956.4,                     {float}                                #
#     'Volume': 4708451                         {int}                                 #
#     }                                                                               #
# ]                                                                                   #
#######################################################################################
# file_path = 'symbols_results.xlsx'
# invalid_df = pd.read_excel(file_path, sheet_name='Valid Symbols')["Valid Symbols"].tolist()
# end_date = datetime.now()
# start_date = end_date - timedelta(days=30)
# start_date_str = start_date.strftime('%Y-%m-%d')
# end_date_str = end_date.strftime('%Y-%m-%d')
# for ticker in invalid_df:
#     data = yf.download(ticker, start=start_date_str, end=end_date_str,interval='5m')
#     df = pd.DataFrame(data)
#     formatted_data = [
#     {
#         "Date": date.strftime('%Y-%m-%d'),
#         "Time": date.strftime('%H:%M:%S'),
#         "Open": round(float(row["Open"]), 3),
#         "High": round(float(row["High"]), 3),
#         "Low": round(float(row["Low"]), 3),
#         "Close": round(float(row["Close"]), 3),
#         "Adj Close": round(float(row["Adj Close"]), 3),
#         "Volume": int(row["Volume"])
#     }
#     for date, row in df.iterrows()
#     ]
#     beautified_json = json.dumps(formatted_data, indent=4)
#     with open('data.txt', 'w') as f:
#         f.write(f"{beautified_json}\n")
#     break
######################################################################################

#######################################################################################
#         Get historical data  for last week with 5 min interval                      #
#   Date          Open         High          Low        Close    Adj Close     Volume #
#                                                                                     #
# [                                                                                   #
#     {'Date': '2024-08-16',                       {date }  %Y-%m-%d'                 #
#     "Time": "09:15:00",                           {time}  '%H:%M:%S')               #
#     'Open': 2937.3,                         {float}                                 #
#     'High': 2960.8,                          {float}                                #
#     'Low': 2916.1,                            {float}                               #
#     'Close': 2956.4,                          {float}                               #
#     'Adj Close': 2956.4,                     {float}                                #
#     'Volume': 4708451                         {int}                                 #
#     }                                                                               #
# ]                                                                                   #
#######################################################################################
# file_path = 'symbols_results.xlsx'
# invalid_df = pd.read_excel(file_path, sheet_name='Valid Symbols')["Valid Symbols"].tolist()
# end_date = datetime.now()
# start_date = end_date - timedelta(days=7)
# start_date_str = start_date.strftime('%Y-%m-%d')
# end_date_str = end_date.strftime('%Y-%m-%d')
# for ticker in invalid_df:
#     data = yf.download(ticker, start=start_date_str, end=end_date_str,interval='5m')
#     df = pd.DataFrame(data)
#     formatted_data = [
#     {
#         "Date": date.strftime('%Y-%m-%d'),
#         "Time": date.strftime('%H:%M:%S'),
#         "Open": round(float(row["Open"]), 3),
#         "High": round(float(row["High"]), 3),
#         "Low": round(float(row["Low"]), 3),
#         "Close": round(float(row["Close"]), 3),
#         "Adj Close": round(float(row["Adj Close"]), 3),
#         "Volume": int(row["Volume"])
#     }
#     for date, row in df.iterrows()
#     ]
#     beautified_json = json.dumps(formatted_data, indent=4)
#     with open('data.txt', 'w') as f:
#         f.write(f"{beautified_json}\n")
#     break
###################################################################################


#######################################################################################
#         Get historical data  for today with 5 min interval                          #
#   Date          Open         High          Low        Close    Adj Close     Volume #
#                                                                                     #
# [                                                                                   #
#     {'Date': '2024-08-16',                       {date }  %Y-%m-%d'                 #
#     "Time": "09:15:00",                           {time}  '%H:%M:%S')               #
#     'Open': 2937.3,                         {float}                                 #
#     'High': 2960.8,                          {float}                                #
#     'Low': 2916.1,                            {float}                               #
#     'Close': 2956.4,                          {float}                               #
#     'Adj Close': 2956.4,                     {float}                                #
#     'Volume': 4708451                         {int}                                 #
#     }                                                                               #
# ]                                                                                   #
#######################################################################################
# file_path = 'symbols_results.xlsx'
# invalid_df = pd.read_excel(file_path, sheet_name='Valid Symbols')["Valid Symbols"].tolist()
# for ticker in invalid_df:
#     data = yf.download(ticker,period='1d',interval='5m')
#     df = pd.DataFrame(data)
#     formatted_data = [
#     {
#         "Date": date.strftime('%Y-%m-%d'),
#         "Time": date.strftime('%H:%M:%S'),
#         "Open": round(float(row["Open"]), 3),
#         "High": round(float(row["High"]), 3),
#         "Low": round(float(row["Low"]), 3),
#         "Close": round(float(row["Close"]), 3),
#         "Adj Close": round(float(row["Adj Close"]), 3),
#         "Volume": int(row["Volume"])
#     }
#     for date, row in df.iterrows()
#     ]
#     beautified_json = json.dumps(formatted_data, indent=4)
#     with open('data.txt', 'w') as f:
#         f.write(f"{beautified_json}\n")
#     break
###################################################################################