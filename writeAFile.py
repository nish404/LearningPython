# 'a' = append
# 'r' = read
# 'w' = write

text = "this is a test to see if I have added text"

with open('test.txt','w') as file:
    file.write(text)
