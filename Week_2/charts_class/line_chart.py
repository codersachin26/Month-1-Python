"""
        line_chart.py, this module containing class called LineChart,
        which is responsible for setting all args & drawing line chart over the screen.
"""

import logging

from Week_1.bar_chart.draw_bar_chart import is_list_of


class LineChart:
    """
    LineChart class is responsible for plotting single line chart using matplotlib.

    LineChart methods:
                1. __init__(self, data, xlabel, ylabel,legend, title):
                        set all args to matplotlib.pyplot.

                2. draw(self):
                        simply plot the single line chart using matplotlib.pyplot.
    """

    def __init__(self, data, xlabel, ylabel,legend, title):
        """
        import matplotlib.pyplot as plt and set all args to it,
        save plt object to new variable called single_line.

        :param data: list[int]
        :param xlabel: str
        :param ylabel: str
        :param legend: str
        :param title: str

        """

        if not is_list_of(float, data) or not isinstance(xlabel,str) or not isinstance(ylabel,str) or not isinstance(legend, str) or not isinstance(title, str):
            logging.error('LineChart.__init__() get called with wrongs data types, expected data: list[int], '
                          'xlabel: str, ylabel: str, legend: str, title: str')
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
        plt.plot(data)
        plt.legend([legend])

        logging.debug('set all args to matplotlib.pyplot plt object')

        # save plt to single_line object
        self.single_line = plt

        logging.debug('saved plt object to self.single_line ')

    def draw(self):
        """
        LineChart.draw() method, show single line chart via calling self.single_line.show() func,
        self.single_line, a reference of matplotlib.pyplot plt object.
        """
        logging.debug('LineChart.draw() method get called')
        self.single_line.show()
        logging.info('successfully draw the Line Chart')
