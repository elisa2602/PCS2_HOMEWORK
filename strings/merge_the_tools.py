def merge_the_tools(string, k):
    spl_str = (string[i:i+k] for i in range(0, len(string), k))
    for i in spl_str:
        arr = []
        arr.append(i[0])
        for j in range(1, len(i)):
            if i[j] in arr:
                continue
            else:
                 arr.append(i[j])
                 
        print(''.join(str(e) for e in arr))
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)