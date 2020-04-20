while(True):
    print("구구단 몇 단을 출력할까요?")
    a=int(input())

    if(a==0):
        print("구구단을 종료합니다.")
        break
    elif(a>9):
        print("잘못 입력했습니다. 0~9 사이의 숫자를 입력해주세요")
        continue
    else:
        for i in range(1, 10):
            mul=a*i
            print(str(a)+'x'+str(i)+'='+str(mul))

