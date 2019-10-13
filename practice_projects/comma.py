spam = ['apples', 'bananas', 'tofu', 'cats' ]


def commamer(arg):
    '''
    The function will combine list in to one string 
    '''
    combo = ''
    for i in arg:
        # Add comma and space to the end of element excluding the last.  
        if i != arg[-1]:
            combo = combo + i + ', '
        # adds 'and' right before the last element
        if i == arg[-1]:
            combo = combo + 'and ' + i 
            
    print(combo)

         



commamer(spam)

