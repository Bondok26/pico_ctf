given_flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"

# 1) Convert each character to ascii
ascii_given_flag = [ord(i) for i in given_flag]

# 2) Separate the rightmost 8 bits from the rest of bits (use bitwise AND) and Change them to ascii
hidden_letters = [chr(i & 255) for i in ascii_given_flag]

# 3) Shift right the given flag characters and add the hidden letters
needed_flag = []
for i in range(len(ascii_given_flag)):
    needed_flag.append(chr((ascii_given_flag[i] >> 8)) + hidden_letters[i])

print("".join(needed_flag))


