import sys
from math import sqrt, floor


class CVEB_tree:
    def __init__(self, w):
        self.w = w
        self.T_min = None
        self.T_max = None
        self.aux = None
        self.children = [None for i in range(0, self.next_w()+1)]
        return

    def __del__(self):
        #self.children = None
        self.aux = None

    def empty(self):
        if ( self.T_min is None ) and ( self.T_max is None ):
            return 1
        else:
            return 0

    def next_w(self):
        return floor(sqrt(self.w))

    def high(self, key):
        return key // self.next_w()

    def low(self, key):
        return key % self.next_w()

    def merge(self, high, low):
        return (high * self.next_w()) + low

    def find(self, key):
        if self.empty():
            return 0
        if self.T_max == key:
            return 1
        if self.T_min == key:
            return 1
        hi, lo = self.high(key), self.low(key)
        if (self.children[hi] is None):
            return 0
        else:
            return self.children[hi].find(lo)


    def insert(self, key):
        if self.empty():
            self.T_min = self.T_max = key
        else:
            if key < self.T_min:
                self.T_min, key = key, self.T_min
            if key > self.T_max:
                self.T_max = key

            if self.w > 2:
                hi, lo = self.high(key), self.low(key)
                if self.children[hi] is None:
                    self.children[hi] = CVEB_tree(self.next_w())
                self.children[hi].insert(lo)
                if self.aux is None:
                    self.aux = CVEB_tree(self.next_w())
                self.aux.insert(hi)
        return
    # end insert

    def find_next(self, x):
        if self.empty() or (self.T_max < x):#empty or greater than max
            return None

        if x <= self.T_min:
            return self.T_min

        hi, lo = self.high(x), self.low(x)
        if (self.children[hi] is not None) and (lo <= self.children[hi].T_max):
            lo_next = self.children[hi].find_next(lo)
            if lo_next is not None:
                return self.merge(hi, lo_next)
            else:
                return None
        else:
            hi_next = self.aux.find_next(hi)
            if hi_next is not None:
                return self.merge(hi_next, self.children[hi_next].T_min)
            else:
                return None
    # end find_next


    def find_prev(self, x):
        if self.empty() or (self.T_min > x):
            return None

        if x > self.T_max:
            return self.T_max
        else:
            hi, lo = self.high(x), self.low(x)
            if (self.children[hi] is not None) and (lo > self.children[hi].T_min):
                lo_next = self.children[hi].find_prev(lo)
                if lo_next is not None:
                    return self.merge(hi, lo_next)
                else:
                    return None
            elif self.aux is not None:
                hi_next = self.aux.find_prev(hi)
                if (hi_next is not None):
                    return self.merge(hi_next, self.children[hi_next].T_max)
                else:
                    if (x > self.T_min):
                        return self.T_min
                    else:
                        return None
            else:
                if (x > self.T_min):
                    return self.T_min
                else:
                    return None
    # end find_prev


    def delete(self, key):
        if key == self.T_min:
            if (self.aux == None) or (self.aux.T_min == None):
                self.T_max = self.T_min = None
            else:
                hi = self.aux.T_min
                lo = self.children[hi].T_min
                self.T_min = lo
                self.children[hi].delete(lo)
                if self.children[hi].T_min == self.children[hi].T_max == None:
                    self.children[hi] = None
                    self.aux.delete(hi)
        elif key == self.T_max:
            if (self.aux == None) or (self.aux.T_max == None):
                self.T_max = self.T_min = None
            else:
                hi = self.aux.T_max
                lo = self.children[hi].T_max
                self.T_max = lo
                self.children[hi].delete(lo)
                if self.children[hi].T_min == self.children[hi].T_max == None:
                    self.children[hi] = None
                    self.aux.delete(hi)
        else:
            hi, lo = self.high(key), self.low(key)
            self.T_min = lo
            self.children[hi].delete(lo)
            if self.children[hi].T_min == self.children[hi].T_max == None:
                self.children[hi] = None
                self.aux.delete(hi)
            pass
    # end delete


if __name__ == '__main__':

    test_veb = CVEB_tree(16)

#Test insertion
    # for i in range(1, 15,2):
    #     test_veb.insert(i)
    test_veb.insert(1)
    test_veb.insert(3)
    test_veb.insert(5)
    test_veb.insert(8)
    test_veb.insert(13)
    test_veb.insert(15)
#Test finding successor
    # for i in range(0, 15):
    #     print(i, test_veb.find(i))
    # for i in range(0, 100):
    #     print(i, test_veb.find_next(i))
    for i in range(0,20):
        print(i, test_veb.find_prev(i))
    # assert(1 == test_veb.find_next(0))
    # assert(test_veb.find_next(2) == 4)
    # assert(test_veb.find_next(4) == 5)
    # assert(test_veb.find_next(3) == 4)
    # assert(test_veb.find_next(6) == 7)
    # print(test_veb.find_next(7))
    # assert(test_veb.find_next(13) == 14)
    # assert(test_veb.find_next(16) == None)
#Test finding predsessor
    # print(test_veb.find_prev(8))
    # print(test_veb.find_prev(4))
    # print(test_veb.find_prev(8))
    # print(test_veb.find_prev(13))
    # print(test_veb.find_next(2))
#Test deletion
    # print(test_veb.find(7))
    # test_veb.delete(7)
    # print(test_veb.find(7))
    # print(test_veb.find(14))
    # test_veb.delete(14)
    # print(test_veb.find(14))
    # print(test_veb.find(7))
    # test_veb.delete(7)
    # print(test_veb.find(7))
    # test_int = 7
    # hi, lo = test_veb.high(test_int), test_veb.low(test_int)
    # print(bin(test_int))
    # print(bin(hi), bin(lo))
    # print(bin(test_veb.merge(hi, lo)))
    pass