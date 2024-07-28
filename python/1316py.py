n = int(input())
cnt = n

for i in range(0,n,1):
    world_f = input()
    seen = set()
    world_s = ''
    for world_f in world_f:
        if world_f != world_s:
            if world_f in seen:
                cnt -= 1
                break
            seen.add(world_f)
        world_s = world_f

print(cnt)
