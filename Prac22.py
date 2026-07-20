def count_above(nums, cutoff):
    total = 0
    for n in nums:
        if n > cutoff:
            total +=1 
    return total 
        
def count_below(nums, cutoff):
    total = 0
    for n in nums:
        if n < cutoff:
            total +=1 
    return total 

print(count_below([5, 80, 22, 91], 50))

print(count_above([5, 80, 22, 91], 50))

