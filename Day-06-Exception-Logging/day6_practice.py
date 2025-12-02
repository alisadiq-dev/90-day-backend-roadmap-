# ===== exception Handling =====
"""
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
" finally block is optional ye har condition par chaly ga "
" agr expect block nahi chal rha hai to else block chal rha hai "
"agr try bloak ma koi error nahi ha tu else block chaly ga "
" agr try block ma error ha tu phie expect block chaly ga "

"""
 # Example 
try:
    x = 5 / 0
    print(x)
except ZeroDivisionError:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")


# ========= logging ========
"""
- logging is useful to track the error or exception or inform,sation . it also heIps in debugging the code
_ pyhton ma logging ko use karny kay keye hum loggiong module use karty han 
- sytntax:
import logging  / from logging import 
============logging.basicConfig() #  most impoetant method in logging=====
--- this method is use to congigd the lofigureng system 
--- it takes two parameters (in key value pair)
--- level = logging.DEBUG
--- format = "%(asctime)s - %(levelname)s - %(message)s"
--- filename = "filename.log"

================= Levels ============
level | numaric value 
NOTESET (0)
DEBUG (10)
INFO (20)
WARNING (30)
ERROR (40)
CRITICAL (50)

===== Methods =====
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
 
 ----- getLogger() method -----
- this method is use to get the logger object 
this method Teturn a loger with the specified name 


"""
