



# timestamp = [27,2, 55, 17, 31, 5, 58, 43, 15, 20, 33, 57, 4, 34, 28, 4, 55, 29, 37, 30, 2, 43, 29, 18, 44]

# top = [44, 7, 21, 20, 34]
# print(len(timestamp))
# answer = 0
# for limit in top:
#     count = 0
#     temp = []
#     if timestamp:
#         for index in range(len(timestamp)-1, -1, -1):
#             if timestamp[index] <= limit:
#                 temp.append(timestamp[index])
#                 del timestamp[index]
#                 answer += 1
#                 count += 1
#                 if count == 5 or not timestamp:
#                     break
#     print(temp)
# print(timestamp)
# print(answer)

#
# timestamp = [27, 55,  31, 58, 43,  57,  55, 37]
# 44 = [ 2, 43, 29, 18, 44]
# 7 = [ 4, 4, 5,2,]
# 21 = [15, 20,17,]
# 20
# 34 = [ 30, 29, 28,34, 33,]
#
# [44, 7, 21, 20, 34]
#
# [27,2, 55, 17, 31, 5, 58, 43, 15, 20, 33, 57, 4, 34, 28, 4, 55, 29, 37, 30, 2, 43, 29, 18, 44]
# [27,2, 55, 17, 31, 5, 58, 43, 15, 20, 33, 57, 4, 34, 28, 4, 55, 29, 37, 30] 5
# [27, 55, 17, 31, 58, 43, 15, 20, 33, 57, 34, 28, 55, 29, 37, 30] 4
# [27, 55, 31, 58, 43, 33, 57, 34, 28, 55, 29, 37, 30] 3
# [27, 55, 31, 58, 43, 33, 57, 34, 28, 55, 29, 37, 30] 0
# [27, 55, 31, 58, 43, 57, 55, 37] 5
# arr = [2, 5, 4, 6, 8]
# x = 3
# arr = [1, 2, 3, 1, 2]
# x = 1
# answer = min(arr[:x])
# result = [answer]
# for i in range(x, len(arr)):
#     if arr[i-x] == answer:
#         if answer != arr[i]:
#             temp = min(arr[i-x+1:i+1])
#             answer = temp
#             result.append(temp)
# print(result)