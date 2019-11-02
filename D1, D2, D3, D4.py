n,t,c =map(int, input().split())
req = input().split()
deps = {}
for i in range (n):
    name = input()
    deps[name] = list(input().split())[1:]
used = set()
order = []
def top_sort(cur):
    used.add(cur)
    for dep in deps[cur]:
        if dep not in used:
           top_sort(dep)
    order.append(cur)
for name in req:
    if name not in used:
       top_sort(name)
print(len(used))
if c == 2:
    print(*order)
