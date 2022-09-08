#Divide el arreglo
def sumaGrupos(nums, i, suma1, suma2):
	if i == len(nums):
	    return suma1 == suma2
	else:
	    return sumaGrupos(nums, i+1, suma1+nums[i], suma2) or sumaGrupos(nums, i+1, suma1, suma2+nums[i])

n = int(input())
nums = [0]*n
for i in range(n):
	nums[i] = int(input())
print(sumaGrupos(nums,0,0,0))
