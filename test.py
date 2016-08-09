s = input()
q = int(input())

for  qi in range(q):
    command = input().split()

    if command[0] == 'print':
        a = command[1]
        b = command[2]
        print(s[a:b + 1])
    elif command[0] == 'reverse':
        a = command[1]
        b = command[2]
        s = s[:a] + reversed(s[a:b + 1]) + s[b + 1:]
    else:
        p = command[3]
        s =