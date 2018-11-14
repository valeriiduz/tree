"""

"""


class Transaction:
    """
    """
    state = None

    def commit(self, obj):
        """

        :param obj:
        :return:
        """
        self.state = obj

    def rollback(self):
        """

        :return:
        """
        return self.state
