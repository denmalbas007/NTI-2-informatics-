n = int(input())
lstr = input().split(" ")
nums = []
i = 0
sum = 0
while i < n:
    nums.append(int(lstr[i]))
    sum += int(lstr[i])
    i += 1
if sum % 5 == 0 and len(nums) > 4:
    tgt_sum = int(sum / 5)
    nums = sorted(nums, reverse=True)
    ps = "Yes"
    cur_sum = 0
    boxes = 0
    b = False
    for cur_num in nums:
        if boxes == 5:
            ps = "No"
            break
        cur_sum += cur_num
        if abs(cur_sum) > abs(tgt_sum):
            ps = "No"
            break
        if cur_sum == tgt_sum:
            break
    print(ps)
else:
    print("No")
