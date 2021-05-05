# x = -5
# assert (x >= 0), 'X is not Positive'

import time 

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 6:
        raise ValueTooSmallError('value is too small', x)
    

if __name__ == '__main__':
    try:
        test_value(5)
    except ValueTooHighError as t:
        print(t)
    except ValueTooSmallError as e:
        print(e)
        print(e.message, e.value)


# try: 
#     a = 5 / 1
#     s = a + 4
#     print(s)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as d:
#     print(d)
# else:
#     print('Everything is fine')
#     print('loading....')
#     time.sleep(5)
# finally:
#     print('Cleaning up...')

