def read_hour():
    return int(input("Enter hour: "))

def read_minute():
    return int(input("Enter minute: "))

def read_second():
    return int(input("Enter second: "))

def to_seconds(h, m, s):
    return (s+m*60+h*3600)

def time_elapsed(start, finish):
    t = finish-start
    h = t//3600
    m = t%3600//60
    s = t%3600%60
    return ("%d hours %d minutes %d seconds." %(h,m,s))
def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))