"""
        histogram_chart.py, this module containing class called HistChart,
        which is responsible for setting all args & drawing histogram chart over the screen.
"""

import logging

from Week_1.bar_chart.draw_bar_chart import is_list_of


class HistChart:
    """
    HistChart class is responsible for plotting frequency distribution aka histogram chart using matplotlib.

    HistChart methods:
                1. __init__(self, data, xlabel, ylabel,legend, title):
                        set all args to matplotlib.pyplot.

                2. draw(self):
                        simply plot the histogram chart using matplotlib.
    """

    def __init__(self, data, xlabel, ylabel,legend, title):
        """
        import matplotlib.pyplot as plt and set all args to it,
        save plt object to new variable called hist.

        :param data: list[float]
        :param xlabel: str
        :param ylabel: str
        :param legend: str
        :param title: str

        """

        if not is_list_of(float, data) or not isinstance(xlabel,str) or not isinstance(ylabel,str) or not isinstance(legend, str) or not isinstance(title, str):
            logging.error('HistChart.__init__() get called with wrongs data types, expected data: list[int], '
                          'xlabel: str, ylabel: str, legend_title: str, title: str')
            return

        try:
            import matplotlib.pyplot as plt
            logging.debug('matplotlib.pyplot imported successfully')
        except ModuleNotFoundError as err:
            logging.error(f'matplotlib.pyplot not able to import, Error: {repr(err)}')
            return

        # setting all args to plt
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.hist(data, label=legend)
        plt.legend()

        logging.debug('set all args to matplotlib.pyplot plt object')

        # save plt to single_line object
        self.hist = plt

        logging.debug('saved plt object to self.hist ')

    def draw(self):
        """
        HistChart.draw() method, show histogram chart via calling self.hist.show() func,
        self.hist is a reference of matplotlib.pyplot plt object.
        """
        logging.debug('HistChart.draw() method get called')
        self.hist.show()
        logging.info('successfully draw the histogram Chart')
