# Changed by main
# Simple generator yielding numbers 0-9
def gen():
    yield from range(10)


# Print generator function and object types
print("gen function:", gen)
print("gen() (generator object):", gen())
print("type(gen):", type(gen))
print("type(gen()):", type(gen()))

# Demonstrate next() on a new generator each time (always starts at 0)
print("next(gen()):", next(gen()))
print("next(gen()):", next(gen()))


# Use a single generator object to iterate through values
gen_ob = gen()
print("gen_ob.__next__():", gen_ob.__next__())
print("gen_ob.__next__():", gen_ob.__next__())
print("gen_ob.__next__():", gen_ob.__next__())
print("gen_ob.__next__():", gen_ob.__next__())
print("gen_ob.__next__():", gen_ob.__next__())
print("gen_ob.__next__():", gen_ob.__next__())


# Generator that chains two sequences
def gen_gen():
    yield from gen()
    yield from range(11, 20)



gen_ob = gen_gen()
print("\nValues from gen_gen():")
try:
    while True:
        print(gen_ob.__next__())
except StopIteration:
    print("End of generator.")