"""
        multi_line_chart.py, this module containing only one class called MultiLineChart,
        which is responsible for drawing multi line chart.
"""

import logging



class MultiLineChart:
    """
    MultiLineChart class is responsible for plotting multi line chart using matplotlib.

    BarChart methods:
                1. __init__(self, data, legend_title, xlabel, ylabel, title):
                        set all args to matplotlib.pyplot.

                2. draw(self):
                        plot the multi line chart using matplotlib.
    """

    def __init__(self, data, legend_title, xlabel, ylabel,title):
        """
        import matplotlib.pyplot as plt and set all args to it,
        save plt object to new variable called multi_chart.

        Parameters
        ----------
        data : dict
            e.g. data = {'btc':[23,23.4,75.6],'litecoin':[230,203.4,705.6]}

        legend_title : str
        xlabel : str
        ylabel : str
        title : str

        """

        try:
            import matplotlib.pyplot as plt
            logging.debug('matplotlib.pyplot imported successfully')
        except ModuleNotFoundError as err:
            logging.error(f'matplotlib.pyplot not able to import, Error: {repr(err)}')
            return

        for label, price in data.items():
            plt.plot(price, label=label)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend(title=legend_title)

        logging.debug('set all args to matplotlib.pyplot plt object')

        # save plt object to bar object
        self.multi_line = plt

        logging.debug('saved plt object to self.multi_line ')

    def draw(self):
        """
        MultiLineChart.draw() method, show multi line chart via calling self.multi_line.show() func,
        self.multi_line, a reference of matplotlib.pyplot plt object.
        """
        logging.debug('MultiLineChart.draw() method get called')
        self.multi_line.show()
        logging.info('successfully draw the multi chart Chart')
