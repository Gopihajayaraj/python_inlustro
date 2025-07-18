nums = [1, 2, 3, 4]

n = len(nums)

even_sum_subsets = []




for i in range(2**n):
  
  subset = []
  
  for j in range(n):
        
    if i & (1 << j):
            
       subset.append(nums[j])
    

  if sum(subset) % 2 == 0:
       
     even_sum_subsets.append(subset)




for s in even_sum_subsets:
    
  print(s)