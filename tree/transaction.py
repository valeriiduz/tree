"""

"""

from copy import copy
from copy import deepcopy


class Transaction(object):
    """A transaction guard.
    This is, in fact, just syntactic sugar around a memento closure.
    """
    deep = False
    state = None

    def commit(self, deep, obj):
        self.state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

        def restore():
            obj.__dict__.clear()
            obj.__dict__.update(self.state)

        return restore

    def rollback(self):
        return self.state
