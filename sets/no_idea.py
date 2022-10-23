from collections import Counter

n, m = map(int, input().split())
el_arr = list(map(int, input().split())) 

el_counter = Counter(el_arr)
el_set = set(el_arr)

like = set(map(int, input().split()))
dislike = set(map(int, input().split()))

in_happy = 0

for i in el_set & like:
    in_happy += el_counter[i]
    
for i in el_set & dislike:
    in_happy -= el_counter[i]
            
print(in_happy)
