# Design a stack that includes a max operation, in addition to push and pop. The max method should return the maxium value stored in the stack.

### Hint : Use additonal storage to track the maxium value.
import collections

class Stack:

    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element','max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max() : empty stack')
        return self._element_with_cached_max

    def pop(self):
        if self.empty():
            raise IndexError('pop () : empty stack')
        return self._element_with_cached_max.pop().element
    
    def push(self,x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max()))
        )


