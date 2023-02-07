H, M = map(int, input().split())
A = H // 10
B = H % 10
C = M // 10
D = M % 10

def hourCheck(A, B):
    return A * 10 + B < 24
def minuteCheck(C, D):
    return C * 10 + D < 60
def updateTime(A, B, C, D):
    newHour = A * 10 + B
    newMinute = C * 10 + D + 1
    if newMinute >= 60:
        newMinute -= 60
        newHour += 1
    if newHour >= 24:
        newHour -= 24
        
    return [newHour, newMinute]

while not (hourCheck(A, C) and minuteCheck(B, D)):
    newTime = updateTime(A, B, C, D)
    A, B = newTime[0] // 10, newTime[0] % 10
    C, D = newTime[1] // 10, newTime[1] % 10

print(str(A * 10 + B) + " " +str(C * 10 + D))
