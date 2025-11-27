# validators.py 
def is_number(value):
    # check user pass a number otherwise it show error 
    try:
        float(value)
        return True
    except:
        return False