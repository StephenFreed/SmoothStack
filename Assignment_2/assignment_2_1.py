# assignment_2_1 questions

# Exercise 3:

# 1
print("~~~~ 1 ~~~~")
print("Hello World"[8])

# 2
print("~~~~ 2 ~~~~")
print("thinker"[2:5])
print("hello"[1])

# 3
print("~~~~ 3 ~~~~")
S = "Sammy"
print(S[2:])

# 4
print("~~~~ 4 ~~~~")
print("".join(set("Mississippi")))

# 5
print("~~~~ palindrome ~~~~")

input_list = ["Stars", "O, a kak Uwakov lil vo kawu kakao!", "Some men interpret nine memos"]
answer = ""

# loops through list of inputs / used list for this problem instead of console input
for line in input_list:
    # strips spaces and punctuation, then sets all characters to lowercase
    stripped_line = ''.join(c for c in line if c.isalnum()).lower()

    # 2 pointer through stripped line
    left_pointer = 0
    right_pointer = len(stripped_line) - 1
    while left_pointer < right_pointer:
        if stripped_line[left_pointer] == stripped_line[right_pointer]:
            left_pointer += 1
            right_pointer -= 1
            if right_pointer == left_pointer:
                answer += "Y "
        else:
            answer += "N "
            break

print(answer)
