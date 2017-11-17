def neeeee():
    from datetime import datetime
    from datetime import time

    current = datetime.now()
    print('The current date and time is:', current)
    print('')

neeeee()

print('Welcome!')
print('')

def ja():
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a*a + b*b == c*c and a + b + c == 1000:
                    print(a, b, c)
                    print('')
                    break

ja()

input("Exit terminal when done.")
