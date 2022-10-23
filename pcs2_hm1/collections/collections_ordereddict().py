from collections import OrderedDict

ordered_dict = OrderedDict()
N = int(input())

for i in range(N):
    item = input().split()
    item_name =' '.join(item[:-1])
    if item_name not in ordered_dict:
        ordered_dict[item_name] = int(item[-1])
    else:
        ordered_dict[item_name] += int(item[-1])
        
for item in ordered_dict:
    print(item, ordered_dict[item])