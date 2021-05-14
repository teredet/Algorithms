def bubble_sort(nums):  
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

# test
random_list_of_nums = [5, 2, 1, 8, 4, 90, 6, 10, 0]  
bubble_sort(random_list_of_nums)  
print(random_list_of_nums)