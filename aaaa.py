
def decorator(fn):
    def _wrapper(*args, **kwargs):
        print("_______________")
        fn(*args, **kwargs)
        print("_______________")

    return _wrapper


@decorator
def my_print(string):
    print(string)

@decorator
def my_print2(string):
    print(string + " ????????? ")




my_print("lkenfrer")
my_print2("lkenfrer")