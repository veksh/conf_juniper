from ansible import errors


#  if len(arr) != len(fields):
#    raise errors.AnsibleFilterError('to_rec: expected %d fields, got %d' % len(fields), len(arr) )
def invert_dict(src):
    """ invert dictionary: {key -> val} to {val -> key} """
    inv = {v: k for k, v in src.iteritems()}
    if len(inv) != len(src):
        raise errors.AnsibleFilterError('invert_dict: cannot invert dict with non-unique values')
    return inv


class FilterModule(object):
    ''' A filter to invert a dictionary to a val -> key mapping '''
    def filters(self):
        return {
            'invert_dict': invert_dict,
            'invert': invert_dict
        }
