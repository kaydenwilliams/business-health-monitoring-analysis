import pandas as pd
import requests
from config import FRED_API_KEY
from sqlalchemy import create_engine
from config import DB_CONNECTION

# Function to fetch a single FRED data series and return it as a DataFrame
def fetch_series(series_id):
    # Build the API request URL using the series code and API key
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"
    
    # Sends the HTTP GET request to the FRED API
    response = requests.get(url)
    
    # Parses the JSON response into a Python dictionary
    data = response.json()
    
    # Extracts the list of data observations from the response
    observations = data['observations']
    
    # Converts observations to a pandas DataFrame
    df = pd.DataFrame(observations)
    
    # Keeps only the date and value columns
    df = df[['date', 'value']]
    
    # Converts value column from string to numeric
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    
    # Tags each row with the series identifier
    df['series_id'] = series_id
    
    return df

# Fetches each economic indicator from the FRED API
df_unemployment = fetch_series('UNRATE')
df_inflation = fetch_series('CPIAUCSL')
df_sentiment = fetch_series('UMCSENT')
print(df_unemployment.head())
print(df_inflation.head())
print(df_sentiment.head())

# Combines all three series into one DataFrame
df_all = pd.concat([df_unemployment, df_inflation, df_sentiment], ignore_index=True)
print(df_all.shape)

# Create database connection
engine = create_engine(DB_CONNECTION)

# Load data into MySQL table
df_all.to_sql('economic_indicators', con=engine, if_exists='replace', index=False)
print("Data loaded to MySQL successfully")