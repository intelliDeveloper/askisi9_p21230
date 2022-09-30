import itertools

'''Αριθμός Μητρώου: Π21230'''
'''Η εκφώνηση δεν λέει να μη χρησιμοποιήσουμε βιβλιοθήκη, οπότε χρησιμοποιούμε την itertools για να πάρουμε
   τους συνδυασμούς αριθμών'''


def pair(lst, t):

    result = [a for i in range(len(lst), 0, -1)
              for a in itertools.combinations(lst, i)
              if sum(a) == t]

    for combs in result:
        for elements in combs:
            if elements in lst:
                lst.remove(elements)
    lst.sort()
    '''Αν θέλουμε να κανουμε print το αποτέλεσμα:'''
    '''print(lst)'''
    '''Για να κάνουμε return τη νέα λίστα:'''
    '''return lst'''

'''Η κλήση της συνάρτησης pair(lst,t) γίνεται:'''
'''pair([1,2,3], 5)'''


