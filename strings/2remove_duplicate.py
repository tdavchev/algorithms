# Remove duplicate characters from a string.
def remove_duplicates(string):
    if not isinstance(string, str):
        return string

    if len(string) < 2:
        return string

    chars = [0 for _ in range(255)]
    for elem in string:
        chars[ord(elem)] = 1

    ans = ''

    for elem in string:
        position = ord(elem)
        if chars[position] == 1:
            ans = ans + elem
            chars[position] = 0

    return ans

# this solution does not require any extra memory
# but runs in O(n^2) time
# Null terminating strings are not used in Java.
# For this question, assume that you are passed a
# null terminated string (array of characters).
def remove_duplicates_2(str):
  write_index = 0
  
  for i in range(len(str)):
    found = False
    
    for j in xrange(0, write_index):
      if str[i] == str[j]:
        found = True
        break

    if found == False:
      str[write_index] = str[i]
      write_index += 1

  str[write_index] = '\0'