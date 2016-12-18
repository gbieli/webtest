def test():
    yield 1
    yield 2
    yield 3

run = 0
for i in test():
    print(i)
    run += 1

print("loop ran:", run, "times")
gen = test()
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen))

def numberGen():
    i = 0
    while True:
        print("current number:", i)
        i += 1
        yield

generator = numberGen()
next(generator)
print("do something")
next(generator)
next(generator)