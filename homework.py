def max_num(a,b,c):
    return max(a,b,c)

def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def rev_string(input_string):
    return input_string[::-1]

def num_within(number, start_range, end_range):
    return start_range <= number <= end_range

def pascal(n):
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            row.extend([prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)])
            row.append(1)
        triangle.append(row)
        print(" " * (n - i - 1) + " ".join(map(str, row)))


print(max_num(52,15,6))
print(max_num(5,415,46))
print(mult_list([2,3,5,7]))
print(rev_string("'I am a servant of the Secret Fire, wielder of the flame of Anor. YOU CAN NOT PASS! The dark fire will not avail you, flame of Udûn. Go back to the Shadow! "))
print(num_within(3,2,4))
print(num_within(10,2,5))
print(pascal(6))