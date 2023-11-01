class OutOfBoundError(Exception):
    pass

try:
    raise OutOfBoundError('You are out of bound')
except OutOfBoundError as e:
    print(e)

