from ansible import errors
import re

def to_dict(rec_arr, key):
    """ convert array of records to dictionary key -> record """
#    if len(arr) != len(fields):
#        raise errors.AnsibleFilterError('to_rec: expected %d fields, got %d' % len(fields), len(arr) )
    return {item[key]: item for item in rec_arr}

def to_dict_flat(rec_arr):
    """ convert array of records to dictionary rec[0] -> rec[1] """
    return {item[0]: item[1] for item in rec_arr}

class FilterModule(object):
    ''' A filter to convert list of records into dict of records '''
    def filters(self):
        return {
            'to_dict' : to_dict,
            'to_dict_flat': to_dict_flat
        }
