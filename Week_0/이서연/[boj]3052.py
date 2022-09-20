'''
나머지

- 문제 요약
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지.
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구하고, 서로 다른 값이 몇개 있는지 출력하는 프로그램

- 입력 조건
첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어짐.
이 숫자는 1000보다 작거나 같고, 음이 아닌 정수이다.

- 출력 조건
첫째 줄에 42로 나누었을 때 서로 다른 나머지가 몇 개 있는지 출력
'''
n = []
for _ in range(10):
    n.append(int(input()) % 42)
result = list(set(n)) # list 중복 제거
print(len(result))