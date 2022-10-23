if __name__ == '__main__':
    N = int(input())
    M = []
    
    for i in range(0, N):
        user_input = input().split()
        if user_input[0] == "insert":
            M.insert(int(user_input[1]), int(user_input[2]))
        elif user_input[0] == "print":
            print(M)
        elif user_input[0] == "remove":
            M.remove(int(user_input[1]))
        elif user_input[0] == "append":
            M.append(int(user_input[1]))
        elif user_input[0] == "sort":
            M.sort()
        elif user_input[0] == "pop":
            M.pop()
        else:
            M.reverse()