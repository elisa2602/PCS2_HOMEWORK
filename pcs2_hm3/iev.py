# 1 = AA-AA, 2 = AA-Aa, 3 = AA-aa, 4 = Aa-Aa, 5 = Aa-aa, 6 = aa-aa 
p_1 = int(input())
p_2 = int(input())
p_3 = int(input())
p_4 = int(input())
p_5 = int(input())
p_6 = int(input())

dom_off_1 = 2
dom_off_2 = 2
dom_off_3 = 2
dom_off_4 = 2*3/4
dom_off_5 = 2*1/2
dom_off_6 = 0

exp_off = p_1*dom_off_1 + p_2*dom_off_2 + p_3*dom_off_3 + p_4*dom_off_4 + p_5*dom_off_5 + p_6*dom_off_6
print(exp_off)