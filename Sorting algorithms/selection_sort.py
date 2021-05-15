def selection_sort(nums):  
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

# test
random_list_of_nums = [5, 2, 1, 8, 4, 90, 6, 10, 0]  
selection_sort(random_list_of_nums)  
print(random_list_of_nums) 