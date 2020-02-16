import time

stored_result = {}


def sum_to_n(n):
    start_time = time.perf_counter()
    result = 0
    for i in reversed(range(n)):
        if i + 1 in stored_result:
            print('Stopping sum at %s because we have previously computed it' % str(i + 1))
            result += stored_result[i + 1]
            break
        else:
            result += i + 1

    stored_result[n] = result
    print(time.perf_counter() - start_time, "seconds")
    return result
