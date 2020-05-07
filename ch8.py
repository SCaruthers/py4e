def chop(t):
    try:
        del t[0]
        del t[len(t)-1]
    except IndexError:
        print('Index error')
    return None

def middle(t):
    return t[1:len(t)-1]
    
print('ch8')
