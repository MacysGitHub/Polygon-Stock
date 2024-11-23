import json
from polygon import RESTClient
import datetime

def main():
    client = RESTClient(api_key="WWOgZSXj7dTJYqYXDIL21oMGt3lZ94k4")
    day = datetime.date.today()
    print(day)
    ticker = "AAPL"
    # List Aggregates (Bars)
    aggs = []
    for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="day", from_=day, to=day,
                              limit=50000):
        aggs.append(a)

    # Extract the opening time from the aggs list
    if aggs:
        print(aggs)
        print(f"open price: {aggs[0].open}")
        opening_time = aggs[0].timestamp  # 't' is typically the timestamp of the aggregate data
        print(f"Opening time for {ticker}: {opening_time}")
    else:
        print(f"No aggregate data found for {ticker} on the specified date.")


main()