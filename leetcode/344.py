# s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

s = ["h","e","l","l","o"]
result_list = []
string_value = "".join(map(str, s))
rev = string_value[::-1]

for i in rev:
    result_list.append(i)

s[:] = result_list

print(s)



