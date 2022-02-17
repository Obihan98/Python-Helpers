# Decorates a function object, returns a decorator object
# Overloads the __call__ method, so that all calls to the
# decorator object increments the call counter, and returns
# the decorated function.
# For recursive function, call counter is the number of recurs.
class track_calls_class():
    def __init__(self, function) -> None:
        self._f = function
        self._calls = 0

    def __call__(self, *args: 'Any', **kwargs: 'Any') -> 'Any':
        self._calls += 1
        return self._f(*args, **kwargs)

    def called(self) -> int:
        return self._calls

    def reset(self) -> None:
        self._calls = 0

# Name factorial now refers to a track_calls object.
@track_calls_class
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Similar to the decorator as class.
def track_calls_func(f):
    def call(*args: 'Any', **kwargs: 'Any') -> 'Any':
        call._calls += 1
        return f(*args, **kwargs)

    call._calls = 0

    return call

@track_calls_func
def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print('')
    print('Factorial is now an object of <track_calls>:', type(factorial), factorial)
    # Calling factorial(3), calls track_calls.__call__(factorial, 3),
    # which increments factorial._calls and then calls factorial._f(3)
    n = 5
    print('Factorial of', n, 'is:', factorial(n))
    print('Factorial function calls itself', factorial.called(), 'times.')

    n = 10
    print('')
    print('Fib is now a function object that track_call_func returns, which is function \'call\':', type(fib), fib)
    print('Fib of', n, 'is:', fib(n))