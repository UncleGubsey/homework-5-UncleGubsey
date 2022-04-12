def remove_duplicates(num_list):
    result = []
    for num in num_list:
        if num not in result:
            result.append(num)
    return result


num_list = [1, 2, 1, 1]
print(remove_duplicates(num_list))
