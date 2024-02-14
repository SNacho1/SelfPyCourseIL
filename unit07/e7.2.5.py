def sequence_del(my_str):
    result = ''
    i = 0
    while i < len(my_str):
        result += my_str[i]
        while i + 1 < len(my_str) and my_str[i] == my_str[i + 1]:
            i += 1
        i += 1
    return result

print(sequence_del("ppyyyyythhhhhooonnnnn"))
print(sequence_del("SSSSsssshhhh"))
print(sequence_del("Heeyyy   yyouuuu!!!"))