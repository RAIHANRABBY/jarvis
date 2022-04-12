# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# !/bin/python3

from datetime import datetime as dt


# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt='%a %d %b %Y %H:%M:%S %z'
    return str(abs(int((dt.strptime(t1, fmt) - dt.strptime(t2, fmt)).total_seconds())))




if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
