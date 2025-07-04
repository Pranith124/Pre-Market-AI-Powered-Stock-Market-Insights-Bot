import app.services
import json

import app.services
import app.services.fetch_india_indices_data

def get_us_summary_ticket(type,interval,lookback_days):
    try:
        if type=="US":
            data_string=app.services.fetch_us_indices_data(interval,lookback_days)
        elif type=="GLOBAL":
            data_string=app.services.fetch_global_indices_data(interval,lookback_days)
        else:
            data_string=app.services.fetch_india_indices_data(interval,lookback_days)
            
        actual_data=[]
        for data in data_string:
            if data.split()[-1]=="None":
                print(data)
            else:
                actual_data.append(data)
        if actual_data:
            try:
                response=app.services.get_ai_stock_summary(data_string=json.dumps(actual_data))
                return response
            except Exception as e:
                raise Exception(f"Filed on fetching the summarey of the data  {str(e)}") from e
        else:
            raise Exception(f"Fiailed to load the data based on the data ")
    except Exception as e:
        print(str(e))