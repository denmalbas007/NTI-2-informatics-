#полное решение
nums = input().split(' ')
n = float(nums[0]) #требуемое количество зданий
e = float(nums[1]) #кол-во энергии, производимое 1 станцией
a = float(input()) #кол-во энергии, требуемое для работы одного здания

if (n*a)%e == 0:
  print(int((n*a)/e))
else:
  print(int((n*a)//e + 1))
