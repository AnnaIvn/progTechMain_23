# checks if input is right. Example of right input: '6: Ben Konrad'
def check_format(arg):
    if arg[0]=='6' or arg[0]=='7' or arg[0]=='8' and len(arg)>= 4:
        return True
    return False


# adds ':' character if it isn't there
def two_dot_formating(arg):
    if arg[1]!=':':
        return str(arg[:1] + ':' + arg[1:])
    return arg


# distributes children amongst classes depending on their age
def distrib_by_age(arg):
    if int(arg[0]) == 6:
        return str(arg + ' -> 1st grade')
    elif int(arg[0]) == 7:
        return str(arg + ' -> 2nd grade')
    elif int(arg[0]) == 8:
        return str(arg + ' -> 3rd grade')
    else:
        return str(arg + ' -> Incorrect age')

