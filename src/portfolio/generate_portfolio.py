from .market_data import Market
import json
import codecs

''' List of currencies to be considered in any portfolio construction (chosen arbitrarily, subject to change later) '''
currencies = ['Bitcoin', 'Ethereum', 'Dash', 'Ripple', 'Monero', 'Litecoin', 'NEM', 'MaidSafeCoin', 'Augur', 'Zcash']

class Portfolio(object):

    ''' Initialize empty portfolio, currency maps to current weight in portfolio { currency : value } '''

    ''' Risk level of portfolio (set by user) '''
    risk_level = 0

    '''' USD cash value of portfolio holdings '''
    holdings_value = 0

    '''' USD cash value of readily available cash (not all funds will always be invested) '''
    cash_value = 0

    ''' Create new portfolio object
        risk_level: integer (1 - 10)
        cash_value: integer (0]
     '''
    def __init__(self, risk_level, portfolio_value):

        # Set class variables, error check
        if (risk_level < 0 | risk_level > 10):
            raise ValueError("Risk level must be within 0 - 10")
        if (portfolio_value < 0):
            raise ValueError("Portfolio value must be greater than 0")
        self.risk_level = risk_level
        self.cash_value = portfolio_value
        self.portfolio = []

        # Generate portfolio holdings
        self.construct_portfolio()

    ''' Construct portfolio considering current market conditions '''
    def construct_portfolio(self):

        ''' This is where algorithm will be implemented to create a portfolio.
            For first iteration algorithm will be simple,
            if user risk level is < 5
                construct portfolio of: Bitcoin, Ethereum, Dash, Ripple, Monero (with hard - coded varying weights)
            if risk level >= 5
                construct portfolio of: Litecoin, NEM, MaidSafeCoin, Augur, Zcash (with hard - coded varying weights)
        '''
        if self.risk_level < 5:
            self.portfolio.append({'name': 'Bitcoin', 'alloc': 4, 'symbol': 'BTC'})
            self.portfolio.append({'name': 'Ethereum', 'alloc': 5, 'symbol': 'ETC'})
            self.portfolio.append({'name': 'DASH', 'alloc': 10, 'symbol': 'DASH'})
            self.portfolio.append({'name': 'Ripple', 'alloc': 10, 'symbol': 'RIP'})
            self.portfolio.append({'name': 'Monero', 'alloc': 5, 'symbol': 'MON'})
            invested_value = ((4 * self.get_price('Bitcoin') + (5 * self.get_price('Ethereum')) + (10 * self.get_price('Dash')) +
                                                 (10 * self.get_price('Ripple')) + (5 * self.get_price('Monero'))))
            self.holdings_value = invested_value
            self.cash_value -= invested_value

        else:
            self.portfolio.append({'name': 'Bitcoin', 'alloc': 7, 'symbol': 'BTC'})
            self.portfolio.append({'name': 'Litecoin', 'alloc': 137, 'symbol': 'LTE'})
            self.portfolio.append({'name': 'NEM', 'alloc': 13, 'symbol': 'NEM'})
            self.portfolio.append({'name': 'MaidSafeCoin', 'alloc': 25, 'symbol': 'MSC'})
            self.portfolio.append({'name': 'Augur', 'alloc': 12, 'symbol': 'AUG'})
            invested_value = ((7 * self.get_price('Bitcoin')) + (137 * self.get_price('Litecoin') +
                                (13 * self.get_price('NEM')) + (25 * self.get_price('MaidSafeCoin'))
                                + (10 * self.get_price('Augur')) + (12 * self.get_price('Zcash'))))
            self.holdings_value = invested_value
            self.cash_value -= invested_value

        return

    ''' Re-balance portfolio considering current market conditions '''
    def balance_portfolio(self):
        #TODO (next iteration)
        return


    def get_total_portfolio_value(self):

        return self.cash_value + self.holdings_value


    ''' Send portfolio to front end for display '''
    def send_portfolio(self):
        #TODO
        return


    ''' Helper function that returns json object of crypto-currencies to consider for portfolio
        used in construction + re-balancing of portfolio object
    '''
    def get_relevant_market_data(self, start, end):

        # Create new market object to get information
        market = Market()

        # Build json object of relevant currency data
        data = {}
        for currency in range(start, end):
            data[currencies[currency]] = market.ticker(currencies[currency])
        json_data = json.dumps(data)
        return data

    ''' Helper function to get current price of currency '''
    def get_price(self, currency):

        # Use market object to obtain latest market data
        market = Market()

        s = codecs.getreader('utf-8')(market.ticker(currency))
        crypto_price = float(json.load(s)[0].get('price_usd'))
        return crypto_price