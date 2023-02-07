N, Q = map(int, input().split())
follower = {}
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        follower[(A, B)] = 1
    elif T == 2:
        follower[(A, B)] = 0
    else:
        if not (A, B) in follower or not (B, A) in follower:
            print("No")
        elif follower[(A, B)] == 1 and follower[(B, A)] == 1:
            print("Yes")
        else:
            print("No")
