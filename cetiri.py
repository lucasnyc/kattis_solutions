ans = sorted([int(num) for num in input().split()])
diff = [abs(ans[i]-ans[i+1]) for i in range(len(ans)-1)]
    
if diff[0] > diff[1]:
    print(min(ans[0],ans[1])+diff[1])
elif diff[0] < diff[1]:
    print(min(ans[1],ans[2])+diff[0])
else: print(max(ans)+ diff[0])

