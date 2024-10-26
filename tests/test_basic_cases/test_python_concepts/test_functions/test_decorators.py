def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("First I'll show My output and then call the wrapper with decoratoed value")
        function(*args, **kwargs)

    return wrapper

@mydecorator
def mywrapper(person):
    print(f"Hi, {person} is the one being decorated.")

mywrapper("Nipun")