import json
import app.services

def fetch_us_indices_data(interval: str = "1m", lookback_days: int = 1) -> str:
    """
    Fetches real-time data for major US market indices and returns as JSON string.
    
    Args:
        interval: Data interval (default: "1m")
        lookback_days: Number of days to look back (default: 1)
        
    Returns:
        str: JSON string containing index data
        
    Example Output:
    '[ "Index: Dow Jones {...}", "Index: Nasdaq {...}" ]'
    """
    US_indices = {
        "Dow Jones": "^DJI",
        "Nasdaq": "^IXIC", 
        "S&P": "^GSPC"
    }
    
    data = []
    for index, ticker in US_indices.items():
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