# 1. 출력() = print()
def 출력(n):
    print(n)
# 2. 절댓값() = abs()
def 절댓값(n):
    return abs(n)
# 3. 최대() = max()
def 최대(n):
    return max(n)
# 4. 최소() = min()
def 최소(n):
    return min(n)
# 5. 정렬() = sorted()
def 정렬(n):
    return sorted(n)
# 6. 길이() = len()
def 길이(n):
    return len(n)
# 7. 목록() = list()
def 목록(n):
    return list(n)
# 8. 범위() = range()
# 범위(), 괄호 안에 세 가지 항목을 무조건 작성해야 한다. 범위(1, 10)로 하면 Error 발생, 범위(1, 10, 1)로 해야 함.
def 범위(n, n1, n2):
    return range(n, n1, n2)
# 9. 유형() = type()
def 유형(n):
    return type(n)
# 10. 이진수() = bin()
def 이진수(n):
    return bin(n)
# 11. 팔진수() = oct()
def 팔진수(n):
   return oct(n)
# 12. 십육진수() = hex()
def 십육진수(n):
   return hex(n)
# 13. 문자열() = str()
def 문자열(n):
    return str(n)
#14. 수열() = int()
def 수열(n):
    return int(n)
#15. 사전() = dict()
def 사전(n):
    return dict(n)
# 16. 입력() = input()
def 입력(n):
    return input(n)
# 16. 합() = sum()
def 합(n):
    return sum(n)
# 17. 판단() = bool()
def 판단(n):
    return bool(n)
# 18. 유니문자() = chr()
def 유니문자(n):
    return chr(n)
# 19. 유니숫자() = ord()
def 유니숫자(n):
    return ord(n)
#20. 열기() = open()
def 열기(n, n1):
    if n1==읽:
        return open(n,‘r’)
    if n1==쓰:
        return open(n,‘w’)
    if n1==편:
        return open(n,‘a’)
    else:
        print(“오류 : 열기(‘파일 이름’, ‘읽, 쓰, 편’)로 입력해주세요.”)
