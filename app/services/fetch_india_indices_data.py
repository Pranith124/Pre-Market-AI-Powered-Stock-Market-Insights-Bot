import json
import app.services

def fetch_india_indices_data(interval: str = "1m", lookback_days: int = 1) -> str:

    india_indices={
        "Nifty 50": "^NSEI",
        "Nifty Bank": "^NSEBANK",
        "Nifty IT": "^CNXIT",
        "Sensex (BSE 30)": "^BSESN"
    }

    
    data = []
    for index, ticker in india_indices.items():
        try:
            index_data = app.services.fetch_index_data(
                ticker,
                interval=interval,
                days_ago=lookback_days
            )
            data.append(f"Index: {index} {str(index_data)}")
        except Exception as e:
            print(f"Failed to fetch {index}: {str(e)}")
            continue
            
    return data