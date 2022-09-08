#Divide el arreglo con multiplos de 3 o 5 
def sumaGrupos(nums, i, suma5, suma3):
    if i == len(nums):
        return suma5 == suma3
    else:
        if nums[i]%5 == 0:
            return sumaGrupos(nums, i+1, suma5+nums[i], suma3)
        elif nums[i]%3 == 0:
            return sumaGrupos(nums, i+1, suma5, suma3+nums[i])
        else:
            return sumaGrupos(nums, i+1, suma5+nums[i], suma3) or sumaGrupos(nums, i+1, suma5, suma3+nums[i])
n = int(input())
nums = [0]*n
for i in range(n):
	nums[i] = int(input())
print(sumaGrupos(nums,0,0,0))
