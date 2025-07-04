from datetime import datetime, timedelta
import yfinance as yf


def fetch_index_data(ticker, interval="1m", days_ago=1):
    try:
        # Calculate date range: one full day before today
        end_date = datetime.now() - timedelta(days=days_ago - 1)
        start_date = end_date - timedelta(days=1)

        # Format dates
        start_str = start_date.strftime('%Y-%m-%d')
        end_str = end_date.strftime('%Y-%m-%d')

        # Fetch historical data
        nifty = yf.Ticker(ticker)
        data = nifty.history(start=start_str, end=end_str, interval=interval)

        if data.empty:
            raise ValueError("No data returned. Market might have been closed on that day.")

        # Reset index for clean datetime column
        data = data.reset_index()
        data['Datetime'] = data['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

        return data  # Return full intraday candle DataFrame

    except Exception as e:
        print(f"[ERROR] Failed to fetch NIFTY50 data: {str(e)}")
        return None
