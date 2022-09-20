import my_module
# from my_module import MY_CONST as some_var
from my_module import my_string as abcd
import new_pkg
from new_pkg.inner_pkg.inner_mod import from_inner_mod



# print(module1.MY_MEGA_CONST)
if __name__ == "__main__":
    MY_CONST = "MEGA VAR!!!"
    print(my_module.MY_CONST)
    print(abcd)
    print(my_module.my_func(2, 3))
    print(MY_CONST)
    print(new_pkg.PKG_EX)
    print(new_pkg.module1.abcd())
    print(from_inner_mod)







