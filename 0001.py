# _*_ coding:utf-8 _*_
import random

# count:随机码数量 length:随机码长度
def PromoCode(count,length):
    promo_code_lst = []
    for i in range(count-1):
        promo_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length-1)
        if promo_code not in promo_code_lst:
        promo_code_list.append(promo_code)
    return promo_code_lst
