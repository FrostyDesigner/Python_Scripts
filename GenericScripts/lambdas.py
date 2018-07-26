#some functions have no names
#called anonymous functions

# write a function to compute 3x + 1

def f(x):
    return 3*x + 1

print(f(2))
print(f(3))
print(f(5))

# now do  it anonymously
g = lambda x: 3*x + 1
print(g(2))
print(g(3))
print(g(5))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("    leonhard", "EULER"))

def build_report(trees):
    return 10 * trees + 20

print(build_report(7))