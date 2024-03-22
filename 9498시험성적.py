
score = int(input()) # 시험 점수를 'score'라는 변수로 지정 'input()'함수로  숫자입력 숫자는 문자형이기 때문에 이를 'int()'로 정수로 변환

if score >= 90:     # 만약 'score'=입력한 숫자가 90보다 크거나 같다면 A를 출력
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:               # 위 모든 사항에 해당하지 않으면 F를 출력
    print('F')