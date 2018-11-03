

def fizzbuzz(number):
    if not isinstance(number, int):
        raise TypeError('')
    if number % 15 == 0:
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number % 5 == 0:
        return 'bazz'
    return str(number)    # ... # v Pythonu object eliptis  - pass tady nic není, ... tady nic není ale jednu tu něco bude
    