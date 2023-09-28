def check_format(arg):
    if arg.isdigit() and arg[1]==':' and int(arg[0])==len(arg)-2:
        return True
    return False

def distrib_by_age(arg):
    if int(arg[0]) == 6:
        return str(arg + ' -> ' + '1st grade')
    elif int(arg[0]) == 7:
        return str(arg + ' -> ' + '2nd grade')
    elif int(arg[0]) == 8:
        return str(arg + ' -> ' + '3rd grade')
    else:
        return str(arg + ' -> ' + 'Incorrect age')

