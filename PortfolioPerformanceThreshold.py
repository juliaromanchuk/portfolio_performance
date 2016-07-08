# Class PortfolioPerformanceThreshold is designed to set risk and return limits
class PortfolioPerformanceThreshold():

    def set_risk_free_rate(self):
        global risk_free_rate
        risk_free_rate = float(raw_input("Please set the risk-free rate in percentage: "))
        return risk_free_rate

    def get_risk_free_rate(self):
        global risk_free_rate
        risk_free_rate = risk_free_rate/float(100)
        return risk_free_rate

    def set_risk_threshold(self):
        global var_threshold
        var_threshold = float(raw_input("Please set the maximum variance of portfolio in percentage: "))
        return

    def get_risk_threshold(self):
        global var_threshold
        var_threshold = var_threshold/float(100)
        return var_threshold

    def set_sharpe_threshold(self):
        global sharpe_threshold
        sharpe_threshold = float(raw_input("Please set the minimum Sharpe Ratio of portfolio in percentage: "))
        return

    def get_sharpe_threshold(self):
        global sharpe_threshold
        sharpe_threshold = sharpe_threshold/float(100)
        return sharpe_threshold

    def set_treynor_threshold(self):
        global treynor_threshold
        treynor_threshold = float(raw_input("Please set the minimum Treynor Ratio of portfolio in percentage: "))
        return

    def get_treynor_threshhold(self):
        global treynor_threshold
        treynor_threshold = treynor_threshold/float(100)
        return treynor_threshold

    def set_alpha_threshold(self):
        global alpha_threshold
        alpha_threshold = float(raw_input("Please set the minimum Jensen's alpha measure of portfolio in percentage: "))
        return

    def get_alpha_threshold(self):
        global alpha_threshold
        alpha_threshold = alpha_threshold/float(100)
        return alpha_threshold

    def set_required_return(self):
        global return_threshold
        return_threshold = float(raw_input("Please set the minimum required return on portfolio in percentage: "))
        return

    def get_required_return(self):
        global return_threshold
        return_threshold = return_threshold/float(100)
        return return_threshold

