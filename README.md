


---
# <span style="color:rgb(0, 32, 96)">MCAP28032024.xlsx</span> 

---

- You can download the latest list of all the listed company in NSE from sit
	- https://www.nseindia.com/regulations/listing-compliance/nse-market-capitalisation-all-companies

### <span style="color:rgb(0, 176, 240)">This is how data looks like:</span>

| Sr No. | Symbol   | Company Name                | Market capitalization as on March 28, 2024<br>(In lakhs) |
| ------ | -------- | --------------------------- | -------------------------------------------------------- |
| 1      | RELIANCE | Reliance Industries Limited | 201056022.448876                                         |

### <span style="color:rgb(0, 176, 240)">First Get all the symbols from the excel</span>

```python
import pandas as pd
import yfinance as yf
df= pd.read_excel("MCAP28032024.xlsx")
df['Symbol'] = df['Symbol'].astype(str) + '.NS'
all_nse_symbols=df["Symbol"].tolist()
```


### <span style="color:rgb(0, 176, 240)">You will get data in this form:</span>

```python
['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'BHARTIARTL.NS', 'SBIN.NS', 'INFY.NS', 'LICI.NS', 'ITC.NS', 'HINDUNILVR.NS', 'LT.NS', 'BAJFINANCE.NS', 'HCLTECH.NS', 'MARUTI.NS', 'SUNPHARMA.NS', 'ADANIENT.NS', 'KOTAKBANK.NS', 'TITAN.NS', 'ONGC.NS', 'TATAMOTORS.NS', 'NTPC.NS', 'AXISBANK.NS', 'DMART.NS', 'ADANIGREEN.NS', 'ADANIPORTS.NS', 'ULTRACEMCO.NS', 'ASIANPAINT.NS', 'COALINDIA.NS', 'BAJAJFINSV.NS', 'BAJAJ-AUTO.NS', 'POWERGRID.NS', 'NESTLEIND.NS', 'WIPRO.NS', 'M&M.NS', 'IOC.NS', 'JIOFIN.NS', 'HAL.NS', 'DLF.NS', 'ADANIPOWER.NS', 'JSWSTEEL.NS', 'TATASTEEL.NS', 'SIEMENS.NS', 'IRFC.NS', 'VBL.NS'
]
```


### <span style="color:rgb(0, 176, 240)">Now use this code to store the valid and invalids symbols in excel file:</span>

```python
import pandas as pd
import yfinance as yf
for ticker in all_nse_symbols:
    data = yf.download(ticker, start="2024-01-01", end="2024-01-03")
    if not data.empty:
        valid_symbols.append(ticker)
    else:
        invalid_symbols.append(ticker)
    break
valid_df = pd.DataFrame(valid_symbols, columns=['Valid Symbols'])
invalid_df = pd.DataFrame(invalid_symbols, columns=['Invalid Symbols'])
with pd.ExcelWriter('symbols_temp.xlsx') as writer:
    valid_df.to_excel(writer, sheet_name='Valid Symbols', index=False)
    invalid_df.to_excel(writer, sheet_name='Invalid Symbols', index=False)
```
Here valid symbols means that you can get historical and live data of these symbols using `yfinance` library 


## <span style="color:rgb(0, 176, 240)">Whole code to store the valid and invalid symbols in excel sheet</span>

```python
import pandas as pd
import yfinance as yf
# Load the Excel file
df = pd.read_excel("MCAP28032024.xlsx")
# Append '.NS' to each symbol to specify it's an NSE stock
df['Symbol'] = df['Symbol'].astype(str) + '.NS'
# Initialize the lists to store valid and invalid tickers
valid_symbols = []
invalid_symbols = []
# Convert the symbols column to a list
all_nse_symbols = df["Symbol"].tolist()
# Loop over each symbol and fetch data using yfinance
for ticker in all_nse_symbols:
    data = yf.download(ticker, start="2024-01-01", end="2024-01-03")
    if not data.empty:
        valid_symbols.append(ticker)
    else:
        invalid_symbols.append(ticker)
    break
# Create a DataFrame for valid and invalid symbols
valid_df = pd.DataFrame(valid_symbols, columns=['Valid Symbols'])
invalid_df = pd.DataFrame(invalid_symbols, columns=['Invalid Symbols'])
# Save the DataFrames to an Excel file with separate sheets
with pd.ExcelWriter('symbols_temp.xlsx') as writer:
    valid_df.to_excel(writer, sheet_name='Valid Symbols', index=False)
    invalid_df.to_excel(writer, sheet_name='Invalid Symbols', index=False)
```

---
# <span style="color:rgb(0, 32, 96)">Get Historical Data:</span>
---

```python
import pandas as pd
import yfinance as yf
import logging
from datetime import datetime, timedelta
import json
file_path = 'symbols_results.xlsx'
invalid_df = pd.read_excel(file_path, sheet_name='Valid Symbols')["Valid Symbols"].tolist()
for ticker in invalid_df:
    data = yf.download(ticker, start="1950-01-01", end=None)
    df = pd.DataFrame(data)
    formatted_data = [
    {
        "Date": date.strftime('%Y-%m-%d'),
        "Open": round(float(row["Open"]), 3),
        "High": round(float(row["High"]), 3),
        "Low": round(float(row["Low"]), 3),
        "Close": round(float(row["Close"]), 3),
        "Adj Close": round(float(row["Adj Close"]), 3),
        "Volume": int(row["Volume"])
    }
    for date, row in df.iterrows()
    ]
    beautified_json = json.dumps(formatted_data, indent=4)
    with open('data.txt', 'w') as f:
        f.write(f"{beautified_json}\n")
```

```python
[
    {
        "Date": "1996-01-01",
        "Open": 14.638,
        "High": 14.717,
        "Low": 14.542,
        "Close": 14.692,
        "Adj Close": 9.302,
        "Volume": 52060684
    },
    {
        "Date": "1996-01-02",
        "Open": 14.656,
        "High": 14.728,
        "Low": 14.47,
        "Close": 14.578,
        "Adj Close": 9.23,
        "Volume": 84371654
    },
]
```

---
# <span style="color:rgb(0, 32, 96)">Get historical data  for last month with 5 min interval</span>
---

```python
import pandas as pd
import yfinance as yf
import logging
from datetime import datetime, timedelta
import json
file_path = 'symbols_results.xlsx'
invalid_df = pd.read_excel(file_path, sheet_name='Valid Symbols')["Valid Symbols"].tolist()
end_date = datetime.now()
start_date = end_date - timedelta(days=30)
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')
for ticker in invalid_df:
    data = yf.download(ticker, start=start_date_str, end=end_date_str,interval='5m')
    df = pd.DataFrame(data)
    formatted_data = [
    {
        "Date": date.strftime('%Y-%m-%d'),
        "Time": date.strftime('%H:%M:%S'),
        "Open": round(float(row["Open"]), 3),
        "High": round(float(row["High"]), 3),
        "Low": round(float(row["Low"]), 3),
        "Close": round(float(row["Close"]), 3),
        "Adj Close": round(float(row["Adj Close"]), 3),
        "Volume": int(row["Volume"])
    }
    for date, row in df.iterrows()
    ]
    beautified_json = json.dumps(formatted_data, indent=4)
    with open('data.txt', 'w') as f:
        f.write(f"{beautified_json}\n")
```

```python
[
    {
        "Date": "2024-07-19",
        "Time": "09:15:00",
        "Open": 3164.35,
        "High": 3167.0,
        "Low": 3148.0,
        "Close": 3149.9,
        "Adj Close": 3149.9,
        "Volume": 0
    },
    {
        "Date": "2024-07-19",
        "Time": "09:20:00",
        "Open": 3148.95,
        "High": 3153.05,
        "Low": 3138.6,
        "Close": 3140.0,
        "Adj Close": 3140.0,
        "Volume": 260929
    },
]
```

---
# <span style="color:rgb(0, 32, 96)">Get historical data  for last week with 5 min interval</span>
---

```python
import pandas as pd
import yfinance as yf
import logging
from datetime import datetime, timedelta
import json
file_path = 'symbols_results.xlsx'
invalid_df = pd.read_excel(file_path, sheet_name='Valid Symbols')["Valid Symbols"].tolist()
end_date = datetime.now()
start_date = end_date - timedelta(days=7)
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')
for ticker in invalid_df:
    data = yf.download(ticker, start=start_date_str, end=end_date_str,interval='5m')
    df = pd.DataFrame(data)
    formatted_data = [
    {
        "Date": date.strftime('%Y-%m-%d'),
        "Time": date.strftime('%H:%M:%S'),
        "Open": round(float(row["Open"]), 3),
        "High": round(float(row["High"]), 3),
        "Low": round(float(row["Low"]), 3),
        "Close": round(float(row["Close"]), 3),
        "Adj Close": round(float(row["Adj Close"]), 3),
        "Volume": int(row["Volume"])
    }
    for date, row in df.iterrows()
    ]
    beautified_json = json.dumps(formatted_data, indent=4)
    with open('data.txt', 'w') as f:
        f.write(f"{beautified_json}\n")
```
```python
[
    {
        "Date": "2024-08-12",
        "Time": "09:15:00",
        "Open": 2937.95,
        "High": 2937.95,
        "Low": 2928.1,
        "Close": 2931.3,
        "Adj Close": 2931.3,
        "Volume": 0
    },
    {
        "Date": "2024-08-12",
        "Time": "09:20:00",
        "Open": 2930.6,
        "High": 2942.15,
        "Low": 2929.75,
        "Close": 2936.75,
        "Adj Close": 2936.75,
        "Volume": 69478
    },
]
```

---
# <span style="color:rgb(0, 32, 96)"> Get historical data  for today with 5 min interval
</span>
---

```python
import pandas as pd
import yfinance as yf
import logging
from datetime import datetime, timedelta
import json
file_path = 'symbols_results.xlsx'
invalid_df = pd.read_excel(file_path, sheet_name='Valid Symbols')["Valid Symbols"].tolist()
for ticker in invalid_df:
    data = yf.download(ticker,period='1d',interval='5m')
    df = pd.DataFrame(data)
    formatted_data = [
    {
        "Date": date.strftime('%Y-%m-%d'),
        "Time": date.strftime('%H:%M:%S'),
        "Open": round(float(row["Open"]), 3),
        "High": round(float(row["High"]), 3),
        "Low": round(float(row["Low"]), 3),
        "Close": round(float(row["Close"]), 3),
        "Adj Close": round(float(row["Adj Close"]), 3),
        "Volume": int(row["Volume"])
    }
    for date, row in df.iterrows()
    ]
    beautified_json = json.dumps(formatted_data, indent=4)
    with open('data.txt', 'w') as f:
        f.write(f"{beautified_json}\n")
```

```python
[
    {
        "Date": "2024-08-16",
        "Time": "09:15:00",
        "Open": 2938.4,
        "High": 2943.55,
        "Low": 2935.9,
        "Close": 2943.2,
        "Adj Close": 2943.2,
        "Volume": 0
    },
    {
        "Date": "2024-08-16",
        "Time": "09:20:00",
        "Open": 2943.45,
        "High": 2955.0,
        "Low": 2943.2,
        "Close": 2953.15,
        "Adj Close": 2953.15,
        "Volume": 139618
    },
]
```

---
