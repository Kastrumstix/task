data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
def calculate_structure_sum(data):
    total_sum = 0
    if isinstance(data, (list, tuple, set)):
        for item in data:
            if isinstance(item, (int, float)):
                total_sum += item
            if isinstance(item, str):
                total_sum += len(item)
            if isinstance(item, (list, tuple, set)):
                total_sum += calculate_structure_sum(item)
            if isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(key, (int, float)):
                        total_sum += key
                    if isinstance(key, str):
                        total_sum += len(key)
                    if isinstance(value, (int, float)):
                        total_sum += value
                    if isinstance(value, str):
                        total_sum += len(value)
    return total_sum
result = calculate_structure_sum(data_structure)
print(result)


#
# for item in data_structure:
#     if isinstance(item, (int, float)):
#         total_sum += item
#     elif isinstance(item, str):
#         total_length += len(item)
#     elif isinstance(item, (list, tuple, set)):
#         for sub_item in item:
#             if isinstance(sub_item, (int, float)):
#                 total_sum += sub_item
#             elif isinstance(sub_item, str):
#                 total_length += len(sub_item)
#             elif isinstance(sub_item, dict):
#                 total_sum += sum(sub_item.values())
#             elif isinstance(sub_item, tuple):
#                 for sub_sub_item in sub_item:
#                     if isinstance(sub_sub_item, (int, float)):
#                         total_sum += sub_sub_item
#                     elif isinstance(sub_sub_item, str):
#                         total_length += len(sub_sub_item)
#                     elif isinstance(sub_sub_item, dict):
#                         total_sum += sum(sub_sub_item.values())
#
# print("Total sum of all numbers:", total_sum)
# print("Total length of all strings:", total_length)
#
# result = calculate_structure_sum(data_structure)
# print(result)
