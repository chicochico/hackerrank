from statistics import mean, median
from bisect import bisect_left


def blackbox(prices, means):
    # flatten prices list
    prices = [p for l in prices for p in l]
    mean = closest(means, median(prices))
    return sum(abs(price - mean) for price in prices)


def parse_input(input):
    prices = [s.split() for s in input[2::2]]
    return [[int(n) for n in l] for l in prices]


def closest(mylist, number):
    '''
    Return the element in the list that
    is closest to the given number
    '''
    mylist.sort()
    pos = bisect_left(mylist, number)
    if pos == 0:
        return mylist[0]
    if pos == len(mylist):
        return mylist[-1]
    before = mylist[pos - 1]
    after = mylist[pos]
    if after - number < number - before:
       return after
    else:
       return before


def mean_normalization(input):
    prices = parse_input(input)
    means = [mean(p) for p in prices]
    return blackbox(prices, means)
