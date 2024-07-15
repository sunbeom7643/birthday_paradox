import math

#계산을 통한 수학적 확률
people_number = 58
print(f"{people_number}번 시행")


def notP(n):
  return math.factorial(365) / (365**n * math.factorial(365 - n))

for i in range(1,people_number):
  print(f"{i}명일 때 {(1-notP(i))*100}%")

