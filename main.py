number = int(input("Entrer votre nombre: "))

number_str = str(number)
length = len(number_str) - 1

sum = 0
res = 0
final_string = ""

def calculate_res(num):
  res = 0
  if sum >= 10:
    num_str = str(num)
    res = int(num_str[0])
    return int(num_str[1]), res
  else:
    return num, res

def check_parity(sum, num):
  if num % 2 == 0:
    return sum
  else:
    return sum + 5


last_number = int(number_str[-1])
sum += (10 - last_number) * 2
returned_value = calculate_res(sum)
sum = returned_value[0]
res = returned_value[1]
final_string = final_string + str(sum)

for i in reversed(range(0, length)):
  right_number = int(number_str[i + 1])
  sum = ((9 - int(number_str[i])) * 2) + (right_number // 2) + res
  sum = check_parity(sum, int(number_str[i]))
  returned_value = calculate_res(sum)
  sum = returned_value[0]
  res = returned_value[1]
  final_string = final_string + str(sum)

final_string = final_string + str(res)
final_string = final_string[::-1]
print(f"{number} x 3 = {final_string}")