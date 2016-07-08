class Portfolio(object):
    def __init__(self, stocks, weights):
        self.stocks = stocks
        self.weights = weights

    def add_stocks(self, stock, weights):
        self.stocks.append(stock)
        self.weights[:] = weights
        return self.stocks

    def remove_stock(self, stocks, weights):
        self.weights = []
        self.stocks.remove(stocks)
        self.weights[:] = weights
        return self.stocks

    def get_stocks(self):
        return self.stocks

    def get_weights(self):
        if sum(self.weights) != 1:
            print "Error: sum of stock weights should equal  to 1"
        else:
            return self.weights
        return