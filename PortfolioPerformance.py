import numpy as np
import pandas as pd
from scipy import stats
from Portfolio import Portfolio
from MarketDataProvider import MarketDataProvider
from PortfolioPerformanceThreshold import PortfolioPerformanceThreshold

# Create an instance of the class PortfolioPerformanceThreshold
threshold = PortfolioPerformanceThreshold()
# Set the required return measures and risk accepted on the portfolio
threshold.set_risk_free_rate()
threshold.set_risk_threshold()
threshold.set_sharpe_threshold()
threshold.set_treynor_threshold()
threshold.set_alpha_threshold()
threshold.set_required_return()
# Get the user inputs by calling appropriate methods of class PortfolioPerformanceThreshold
risk_free_rate = threshold.get_risk_free_rate()
var_limit = threshold.get_risk_threshold()
sharpe_limit = threshold.get_sharpe_threshold()
treynor_limit = threshold.get_treynor_threshhold()
alpha_limit = threshold.get_alpha_threshold()
return_limit = threshold.get_required_return()

## Defince a class StockPerformance to calculate stock returns, mean and variance
class StockPerformance():
    def get_stock_returns(self):
        stock_returns = np.log(stock_prices/stock_prices.shift(1))
        stock_returns.drop(stock_returns.head(1).index, inplace=True)
        return stock_returns

    def get_index_mean(self):
        columns = benchmark_returns.columns.values
        index_mean = benchmark_returns[columns].mean() * 252
        return index_mean.__float__()

    def get_index_variance(self):
        column = benchmark_returns.columns.values
        index_variance = benchmark_returns[column].var() * np.sqrt(252)
        return index_variance

## Define a class PortfolioPerformance and include a list of methods to get portfolio performance measures

class PortfolioPerformance(StockPerformance):
    def get_expected_portfolio_return(self):
        annualized_mean = stock_returns.mean() * 252
        ex_portfolio_return = np.sum(annualized_mean * weights)
        return ex_portfolio_return

    def get_portfolio_variance(self):
        weights_adj = np.array(weights)
        port_variance = np.dot(weights_adj.T, np.dot(stock_returns.cov()*252, weights))
        return port_variance

    def get_portfolio_standard_deviation(self):
        weights_adj = np.array(weights)
        port_st_deviation = np.sqrt((np.dot(weights_adj.T, np.dot(stock_returns.cov()*252, weights))))
        return port_st_deviation

    def get_portfolio_sharpe_ratio(self):
        port_sharpe_ratio = (ex_port_return - risk_free_rate)/port_st_deviation
        return port_sharpe_ratio

    def get_portfolio_beta(self):
        port_weighted_daily_return = pd.DataFrame(stock_returns, columns=stocks)
        weights_adj = pd.Series(weights, index=stocks)
        port_weighted_daily_return["Portfolio Weighted Daily Return"] = (stock_returns * weights_adj).sum(1)
        returns = np.array(port_weighted_daily_return["Portfolio Weighted Daily Return"])
        m_returns = np.array(benchmark_returns["^GSPC"])
        slope, intercept, r_value, p_value, std_err = stats.linregress(returns, m_returns)
        return slope

    def get_portfolio_treynor_measure(self):
        port_treynor_measure = float((ex_port_return - risk_free_rate))/beta
        return port_treynor_measure

    def get_portfolio_alpha_measure(self):
        port_alpha_measure = ex_port_return - (risk_free_rate + beta*(market_portfolio_expected_return - risk_free_rate))
        return port_alpha_measure

## Refer to class Portfolio
# create a portfolio consisting of several stocks
portfolio = Portfolio(["GOOGL", "AAPL", "MSFT"], [0.3, 0.4, 0.3])
# let us add a new stock to portfolio with new weights: sum of weights should equal to 1
portfolio.add_stocks("^DJI", [0.2, 0.2, 0.4, 0.2])
# get a list of stocks within the portfolio
stocks = portfolio.get_stocks()

# get a list of weights of the stocks within the portfolio
weights = portfolio.get_weights()


## Refer to class MarketDataProvider to get market data for stocks selected for the portfolio
# define an instance of class MarketDataProvider()
provider = MarketDataProvider()
# retrieve stock prices for the period from yahoo
stock_prices = provider.import_market_data(stocks, "1/1/2015", "7/1/2015")

## Refer to class StockPerformance
stock_performance = StockPerformance()
# get stock returns for the portfolio
stock_returns = stock_performance.get_stock_returns()

## Refer to class PortfolioPerformance
port_performance = PortfolioPerformance()
# get expected return on the portfolio
ex_port_return = port_performance.get_expected_portfolio_return()
# get portfolio variance
port_variance = port_performance.get_portfolio_variance()
# get portfolio standard deviation
port_st_deviation = port_performance.get_portfolio_standard_deviation()

# Let us choose S&P 500 as a proxy for market portfolio
# get the S&P 500 historical returns for the same period as the returns of stocks within the portfolio
# Refer to class MarketDataProvider to get historical market data for S&P 500
stock_prices = provider.import_market_data(["^GSPC"], "1/1/2015", "7/1/2015")
# Calculate returns on market portfolio
benchmark_returns = stock_performance.get_stock_returns()
# Calculate market expected return
market_portfolio_expected_return = stock_performance.get_index_mean()
# Calculate variance on the market portfolio
market_portfolio_variance = stock_performance.get_index_variance()

## refer to class PortfolioPerformance and call appropriate methods to get portfolio performance measures
#Calculate Sharpe Ratio of the Portfolio
port_sharpe_ratio = port_performance.get_portfolio_sharpe_ratio()
## Calculate portfolio beta
beta = port_performance.get_portfolio_beta()
#Calculate Treynor measure of the portfolio
port_treynor_ratio = port_performance.get_portfolio_treynor_measure()
#Calculate Jensen's alpha for the portfolio
port_alpha_ratio = port_performance.get_portfolio_alpha_measure()

## define a function to aggregate the portfolio performance and compare it to specified benchmarks
def show_simulated_portfolio_performance():
    if port_variance <= var_limit:
        var_status = "Accept"
    else:
        var_status = "Reject"

    if port_sharpe_ratio >= sharpe_limit:
        sharpe_status = "Accept"
    else:
        sharpe_status = "Reject"

    if port_treynor_ratio >= treynor_limit:
        treynor_status = "Accept"
    else:
        treynor_status = "Reject"

    if port_alpha_ratio >= alpha_limit:
        alpha_status = "Accept"
    else:
        alpha_status = "Reject"

    if ex_port_return >= return_limit:
        return_status = "Accept"
    else:
        return_status = "Reject"

    indexes = pd.Series(["Variance", "Portfolio Beta", "Expected Portfolio Return", "Sharpe", "Treynor",
                        "Alpha", "Risk Free Rate", "Expected Return on Market Portfolio"])

    data = [[port_variance, var_limit, var_status], [beta, "NaN", "NaN"], [ex_port_return, return_limit, return_status],
            [port_sharpe_ratio, sharpe_limit, sharpe_status], [port_treynor_ratio, treynor_limit, treynor_status],
            [port_alpha_ratio, alpha_limit, alpha_status], [risk_free_rate, "NaN", "NaN"], [market_portfolio_expected_return,
                                                                                           "NaN", "NaN"]]
    portfolio_performance = pd.DataFrame(data, index=indexes, columns=["Value", "Target", "Decision"])
    print portfolio_performance

show_simulated_portfolio_performance()

