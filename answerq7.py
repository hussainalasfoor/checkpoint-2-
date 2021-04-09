import math
num = input("Provide D , if more than one value , split with comma: ")
num = num.split(",")
result_list = []
for D in num:
  Q = round(math.sqrt(2 * 50 * int(D) / 30)); result_list.append(Q)
print(result_list)
