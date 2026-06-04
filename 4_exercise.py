# # comprehension
some_list=['a','b','c','d','e','a','m','n','o','p','m','n','o','p']
# duplicates=[]
# for item in some_list:
#     if some_list.count(item)>1:
#         if item not in duplicates:
#             duplicates.append(item)
# print(duplicates)


duplicates=list(set(item for item in some_list if some_list.count(item)>1 ))
print(duplicates)