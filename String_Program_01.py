def alterString(ip_string,move_letter):
    ip_list = list(ip_string)
    string_length = len(ip_list)
    op_string = []
    move_end = []
    #print(string_length)
    for i in range(string_length):
        if ip_list[i] == move_letter:
            move_end.append(ip_list[i])
        else:
            op_string.append(ip_list[i])
    op_string = op_string + move_end
    str1 = ""
    return str1.join(op_string)

if __name__ == "__main__":
    ip_string = input()
    move_letter = input()
    op_string = alterString(ip_string,move_letter)
    print(op_string)
