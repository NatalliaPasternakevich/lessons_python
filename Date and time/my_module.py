# my_mod.py
# comment
#import time

#time.sleep()
MY_CONST = 123
my_string = '123'
my_dict = {'a_key': 'the value'}

def my_func(abc: int, bcd: str) -> float:
    """Prints and `returns`

    Args:
        abc (int): descr for int
        bcd (str): desct for srt

    Returns:
        float: BMI
    """
    print('What was printed from my func')
    return 2.0

class MyClass:
    my_property = 'my property'
    
    def my_method(self, inp):
        print(self.my_property + ' ' + inp)
# import my_mod

if __name__ == "__main__":
    my_func(2, 3)