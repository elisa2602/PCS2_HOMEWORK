if __name__ == '__main__':
    n = int(input())
    int_lst = map(int, input().split())
    
    t = tuple(int_lst)
    print(hash(t))