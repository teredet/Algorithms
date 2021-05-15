def insertion_sort(nums):  
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

# test
random_list_of_nums = [5, 2, 1, 8, 4, 90, 6, 10, 0]  
insertion_sort(random_list_of_nums)  
print(random_list_of_nums)