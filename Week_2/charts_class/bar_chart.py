"""
        bar_chart.py, this module containing class called BarChart,
        which is responsible for drawing bar chart.
"""

import logging

from Week_1.bar_chart.draw_bar_chart import is_list_of


class BarChart:
    """
    BarChart class is responsible for plotting bar chart using matplotlib.

    BarChart methods:
                1. __init__(self, data, labels, xlabel, ylabel, title):
                        set all args to matplotlib.pyplot.

                2. draw(self):
                        plot the bar chart using matplotlib.
    """

    def __init__(self, data,labels, xlabel, ylabel,title):
        """
        import matplotlib.pyplot as plt and set all args to it,
        save plt object to new variable called bar.

        :param data: list[float]
        :param labels: list[str]
        :param xlabel: str
        :param ylabel: str
        :param title: str

        """

        if not is_list_of(float, data) or not is_list_of(str, labels) or not isinstance(xlabel,str) or not isinstance(ylabel,str) or  not isinstance(title, str):
            logging.error('HistChart.__init__() get called with wrongs data types, expected data: list[int], '
                          'labels: list[str] '
                          'xlabel: str, ylabel: str, title: str')
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
        plt.bar(labels, data)

        logging.debug('set all args to matplotlib.pyplot plt object')

        # save plt object to bar object
        self.bar = plt

        logging.debug('saved plt object to self.bar ')

    def draw(self):
        """
        BarChart.draw() method, show bar chart via calling self.bar.show() func,
        self.bar, a reference of matplotlib.pyplot plt object.
        """
        logging.debug('BarChart.draw() method get called')
        self.bar.show()
        logging.info('successfully draw the bar Chart')
