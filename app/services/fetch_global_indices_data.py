import json
import app.services

def fetch_global_indices_data(interval: str = "1m", lookback_days: int = 1) -> str:

    global_indices={
    "Brent Crude Oil": "BZ=F",
    "Dollar Index (DXY)": "DX-Y.NYB",
    "USD/INR Offshore NDF": "USDINR=X",
    "India VIX": "^INDIAVIX"
    }

    
    data = []
    for index, ticker in global_indices.items():
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