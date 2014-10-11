#	https://www.codeeval.com/public_sc/6/
__author__ = 'frost'

import sys
from bisect import bisect_right, bisect_left


MAX_INT = sys.maxsize
MIN_INT = ~MAX_INT

# def get_words(sfname):
# 	f = open(sfname, "r")
# 	for l in f.read():
# 		wrd_list.append()
# 	return

max_str = ""
L = []


def main(res_str, wrd1, wrd2):
    global max_str
    if (wrd1 == "") or (wrd2 == ""):
        if len(max_str) < len(res_str):
            max_str = res_str
            res_str = ""
            return 0
    elif wrd1[0] == wrd2[0]:
        res_str = res_str + wrd1[0]
        return 1 + main(res_str, wrd1[1:], wrd2[1:])
    else:
        return max(main(res_str, wrd1[1:], wrd2), main(res_str, wrd1, wrd2[1:]))


def bin_search(X, M, L, x):
    lo = 1
    hi = L
    while lo <= hi:
        mid = (lo + hi) // 2
        if X[M[mid]] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


def long_inc_subseq(X):
    llen = len(X)
    d = [MAX_INT for i in range(1, llen + 1)]
    d[0] = MIN_INT
    P = [-1 for i in range(0, llen)]
    M = [-1 for i in range(0, llen)]

    L = 0
    for (i, x) in enumerate(X):
        newL = bisect_left(d,x)
        P[i] = M[newL-1]
        if L < newL:
            L = newL
            d[newL] = x
            M[newL] = i
        elif x < d[newL]:
            d[newL] = x
            M[newL] = i
        # print(d)

    #res = [-1 for i in range(0, L)]
    # print(P)
    # print(M)
    res = []

    k = M[L]
    for i in range(L,0,-1):
        res.append(X[k])
        k = P[k]

    res.reverse()
    return res


def solve2(wrd1, wrd2):
    max_str = ''
    lind = []
    for x in wrd1:
        for (j, y) in enumerate(wrd2):
            if y == x:
                lind.append(j)

    mind = long_inc_subseq(lind)
    print(mind)
    for i in mind:
        max_str += wrd2[i]
    return max_str


if __name__ == '__main__':
    #d = main(res_str, "FXMJQ", "XQMJ")
    #d = main(res_str, "nematode knowledge", "empty bottle")
    #substr = main("QXMJEWFYFDSFABFUZSADG", "QMZJASFAGSGWXASGSDUFDSG")
    #wrd1 = "nematode knowledge"
    #wrd2 = "nempty bottle"
    #wrd1 = "nematode"
    #wrd2 = "mptynade"
    wrd2 = "XMJYAWUZ"
    wrd1 = "MZJAWXU"
    max_str = solve2(wrd1, wrd2)
    print(max_str)
    #test = [0,8,4,12,2,10,6,14]
    # test = [0, 5, 0, 2, 4, 3, 6, 1, 6]
    # res_l = long_inc_subseq(test)
    # print("res =", res_l)






