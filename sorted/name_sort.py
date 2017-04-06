# -*- coding: utf-8 -*-

#按名字排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def ny_name(t):
        return t[0]

L2 = sorted(L, key=by_name)
print(L2)

