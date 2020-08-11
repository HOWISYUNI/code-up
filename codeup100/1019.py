year, month, day = map(int,input().split('.'))
print("%04d.%02d.%02d" %(year,month,day))
input_str = input()
print("%10s" %(input_str))

#print 형식
    # 복잡하지 않으면 : f-string으로 처리한다.
    # 복잡하면 : 형식지정자를 사용한다

# 형식지정자
    # "%가d"  "%가.나f"  "%가s" 형태
    # 가 == 소숫점 포함 전체 출력 자리 수
    # 나 == 소숫점 자릿수
    # 0가 == 가,나 정보로 채우고 나머지 빈칸은 0으로 채워