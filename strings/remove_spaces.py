def remove_spaces(string):
    read_idx = 0
    write_idx = 0

    while read_idx < len(string):
        if string[read_idx] == " ":
            string = string[:read_idx] + string[read_idx + 1:]

        read_idx += 1
   
    return string

a = remove_spaces("az sum bulgarche")
print(a)