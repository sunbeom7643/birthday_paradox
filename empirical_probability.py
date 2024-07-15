import random

from tqdm import tqdm

#100만번 시행을 통한 통계적 확률
trials = 10**6
people_number = 30
same_sum = 0
print(f"{trials}번, {people_number}명")


def trial(people):
  same = 0
  check_birthday = set()
  for _ in range(people):
   check_birthday.add(random.randint(1,365))
    
  if len(check_birthday) == people:
    same += 0
  else:
    same += 1
  return same


for _ in tqdm(range(trials)):
  same_sum += trial(people_number)

print(f"확률은 약 {(same_sum / trials)*100}% 입니다")
