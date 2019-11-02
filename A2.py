#полное решение
nums = input().split(' ')
n = int(nums[0]) #требуемое количество зданий
e = float(nums[1]) #кол-во энергии, производимое 1 станцией
a = 0 #кол-во энергии, потребляемое всеми электростанциями
nums = input().split(' ')

for i in range(n):
  a += int(nums[i])

if (n*a)%e == 0:
  print(int((a)/e))
else:
  print(int(a//e + 1))
