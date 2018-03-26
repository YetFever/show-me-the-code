# _*_ coding:utf-8 _*_
import random

# count:随机码数量 length:随机码长度
def PromoCode(count, length):
    promo_code_lst = []
    while(len(promo_code_lst) < count):
        promo_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        if promo_code not in promo_code_lst:
            promo_code_lst.append(promo_code)
    return promo_code_lst
