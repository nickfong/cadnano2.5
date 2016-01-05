import numpy as np
"""
inner1d(a, a) is equivalent to np.einsum('ik,ij->i', a, a)
equivalent to np.sum(a*a, axis=1)
but faster
"""
from numpy.core.umath_tests import inner1d

def generateVirtualHelixCoordinates(x, y, num_bases):
    """ takes an x, y helical axis center and generates
    coordinates in the z-direction for the average
    phosphate projection bewtween the forward and
    reverse strand on the helical axis. starting from z = 0

    Every points x, y should be the same
    returns: [(x, y, z_i), ...] for i in range(num_bases)
    """
    pass
# def

def generatePhosphateCoordinates(x, y, num_bases, is_5_to_3):
    """ takes and x, y helical axis center and generates
    coordinates of the phosphate position from 5' to 3' on
    the helical axix if is_5_to_3 is True
    otherwise it should be 3' to 5'
    the first element in the list should start at starting from z = 0
    for both cases such that z is monotonically increasing with
    list index

    returns: [(x_i, y_i, z_i), ...] for i in range(num_bases)
    """
    pass
# def

class VirtualHelixArray(object):
    def __init__(self):
        self.coords = np.zeros((0, 2), dtype=float))
        self._query_cache = {}
        self.removed_set = set()
    # end def

    def addCoordinate(self, x, y, idx):
        coords = self.coords
        len_coords = len(coords)
        self._query_cache = {} # clear cache

        if len_coords > idx:    # insert
            self.removed_set.remove(idx)
            coords[idx] = x, y
        elif len_coords == idx:
            new_rows = np.array((x, y), dtype=float))
            self.coords = np.append(coords, new_rows)
        else:
            new_rows = np.zeros((idx - len_coords + 1, 2), dtype=float)
            coords =  np.append(coords, new_rows)
            coords[idx, :] = x, y
            self.coords = coords
    # end def

    def removeCoordinate(self, idx):
        coords = self.coords
        len_coords = len(coords)
        if idx < len_coords:
            self._query_cache = {} # clear cache
            self.removed_set.add(idx)
    # end def

    def truncateCoordinates(self, idx):
        """ idx: the index of the first coordinate to truncate at
        """
        self.coords = self.coords[:idx, :]
        removed_set = self.removed_set
        removed_list = list(removed_set)
        for item in removed_list:
            if item >= idx:
                removed_set.remove(item)
    # end def

    def queryPoint(self, x, y, radius):
        qc = self._query_cache
        query = (x, y, radius)
        if query in self._query_cache:
            return qc.get(query)
        else:
            res = set(self._queryPoint(x, y, radius))
            res.difference(self.removed_set)
            qc[query] =  res
            return res
    # end def

    def _queryPoint(self, x, y, radius):
        """ return the indices of all virtual helices closer
        than radius
        """
        difference = self.coords - (x, y)
        # compute square of distance to point
        delta = inner1d(difference, difference)
        close_points = np.where(delta < radius*radius)
        return close_points[0]
    # end def
# end class

