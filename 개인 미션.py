import random

print('다음 구구단을 풀어주세요! 총 10문제가 제공됩니다.')

score = 0

for i in range(1,11) :
  a = random.randint(1,9)
  b = random.randint(1,9)
  print(a, 'x',  b, '=')
  x = input('답 : ')

  if a * b == int(x) :
    score = score + 1
    print('정답입니다!')
  else :
    print('틀렸습니다!')

print('당신의 점수는 ', score, '점 입니다.')
