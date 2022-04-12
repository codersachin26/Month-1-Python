"""
        pie_chart.py, this module containing class called PieChart,
        which is responsible for setting all args & drawing pie chart over the screen.
"""

import logging

from Week_1.bar_chart.draw_bar_chart import is_list_of


class PieChart:
    """
    PieChart class is responsible for plotting pie chart over the screen.

    PieChart methods:
                1. __init__(self, data, labels, legend_title, title):
                        set all args to matplotlib pyplot.

                2. draw(self):
                        simply plot the pie chart using matplotlib.
    """

    def __init__(self, data, labels, legend_title, title):
        """
        import matplotlib.pyplot and set all args to it,
        save plt object to new variable called pie.

        :param data: list[int]
        :param labels: list[str]
        :param legend_title: str
        :param title: str

        """

        logging.debug('PieChart.__init__(self, data, labels, legend_title, title) method get called')

        if not is_list_of(int, data) or not is_list_of(str, labels) or not isinstance(legend_title, str) or not isinstance(title, str):
            logging.error(
                f'PieChart.__init__() get called with wrongs data types, expected data: list[int], labels: list[str], '
                f'legend_title: str, title: str')
            return

        try:
            import matplotlib.pyplot as plt
            logging.debug('matplotlib.pyplot import successfully')
        except ModuleNotFoundError as err:
            logging.error(f'matplotlib.pyplot not able to import, Error: {repr(err)}')
            return

        # setting all args to plt
        plt.title(title)
        plt.legend(title=legend_title)
        plt.pie(data, labels=labels, autopct='% 1.1f %%', shadow=True)
        logging.debug('set all args to matplotlib.pyplot plt object')

        # save plt object
        self.pie = plt
        logging.debug('saved plt object to self.pie ')

    def draw(self):
        """
        PieChart.draw() method, show pie chart via calling self.pie.show() func,
        self.pie a reference of matplotlib.pyplot plt object.
        """
        logging.debug('PieChart.draw() method get called')
        self.pie.show()
        logging.info('successfully draw the Pie Chart')
