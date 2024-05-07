def cumulative_sum(arr):
    result = []
    total = 0
    for num in arr:
        total += num
        result.append(total)
    return result

# Example usage
my_array = [1, 2, 3, 4, 5]
cumulative_result = cumulative_sum(my_array)
print(cumulative_result)