# Class MarketDataProvider with one method inside is designed to import historical market data
# for any number of stocks and return a daily closes prices per each stock as a data frame
import pandas as pd
from pandas_datareader import data


class MarketDataProvider(object):
    def import_market_data(self, stocks, start_date, end_date, data_source="yahoo"):
        stock_closes_prices = pd.DataFrame()
        for i in range(0, len(stocks)):
            market_prices = data.DataReader(stocks[i], data_source=data_source, start=start_date, end=end_date)
            stock_closes_prices[stocks[i]] = market_prices['Adj Close']
        return stock_closes_prices