# Given a null terminated string, remove any white spaces (tabs or spaces).
def remove_spaces(string):
    if not isinstance(string, str):
        return string

    if len(string) < 1:
        return string

    ans = ''

    for i in range(len(string)):
        if string[i] != ' ' and string[i] != '\t':
            ans = ans + string[i]

    return ans

def remove_spaces_fast(string):
    if not isinstance(string, str) or len(string) < 1:
        return string

    end = 0
    temp_end = 0

    while end < len(string) - 2:
        for i in range(end, len(string)-1):
            if string[i] == ' ' or string[i] == '\t':
                string = string[:i] + string[i+1:]
                temp_end = i
                break
            else:
                temp_end += 1
        end = temp_end

    if string[-1] == ' ' or string[-1] == 't':
        string = string[:-1]

    return string

# Null terminating strings are not used in Python.
# For this question, assume that you are passed a
# null terminated string (array of characters).
# if char list
def remove_white_spaces (s):
  if s == None or len(s) == 0 or s[0] == '\0':
    return

  read_ptr = 0
  write_ptr = 0
  while read_ptr < len(s) and s[read_ptr] != '\0':
    # Lets assume that there are only two 
    # white space characters space and tab.
    if s[read_ptr] != ' ' and s[read_ptr] != '\t':
      s[write_ptr] = s[read_ptr]
      write_ptr += 1
    read_ptr += 1

  # Let's mark the end of string.
  s[write_ptr]= '\0'