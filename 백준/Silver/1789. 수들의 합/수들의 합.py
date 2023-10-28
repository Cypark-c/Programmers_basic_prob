S=int(input()) # 주어진 자연수의 합
'''
서로 다른 자연수인데 일단 연속한다는 제한 사항은 없음.
최대한 많은 자연수로 S를 만드는게 핵심→더하려는 수가 작을 수록 유리
1+....+19=(20*19)/2=190
'''
conti_s=0
i=1
while True:
    if (conti_s+i<S)&(conti_s+i+i+1<=S): # 이 조건 설정에 주의
        conti_s += i
        i+=1
    else:
        break

print(i)
'''
위의 내용으로 연속된 자연수들의 합 중에서 S보다 작은 자연수를 알 수가 있음.
예를들어 200이라고 하면 1~19까지 더한 값은 190인데 10이라는 건 기존에 존재하던 수의
조정을 통해 채워야 함. 그 조정하는 수라는게 마지막에 더한 i보다 작다면, 더 이상 조정할 값은 x
그런데 항상 그러지 않나?
'''