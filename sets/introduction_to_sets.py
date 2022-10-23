def average(array):
   set_arr = set(array)
   S = len(set_arr)
   summy = sum(set_arr)
   return summy/S
   
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)