def duplicate(rec_arr):
    """ get duplicates from list """
    return list(set([x for x in rec_arr if rec_arr.count(x) > 1]))

class FilterModule(object):
    ''' A filter to get duplicates from list '''
    def filters(self):
        return {
            'duplicate' : duplicate
        }

