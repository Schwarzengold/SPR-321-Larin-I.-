def fix_negative_params(func):
    def wrapper(*args):
        print("\nDefault args:", args)
        fixed_args = []
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:  
                fixed_args.append(abs(arg))
            else:
                fixed_args.append(arg)  
        fixed_args = tuple(fixed_args)  
        return func(*fixed_args)
    return wrapper

@fix_negative_params
def my_function(*args):
    print("\nFunction executed with arguments:", test_args, "to", args,"\n")


test_args = (10, -3, "red", -1, 200)
my_function(*test_args)
