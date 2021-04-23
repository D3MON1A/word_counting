import re

# open, reading and closing a file
f = open("texto.txt", "r")
data =f.read()
lowercase = data.lower()
f.close()



# removing spaces
words = re.split(' |\n|:|"|;|\.|\'|!|\?|,|>|<|[0-9]|\(|\)', lowercase)
# counting the words
num_words = len(words)

print("The number of words is ", num_words)

new_words = []

for word in words:
    if word not in new_words:
        new_words.append(word)
        
        
print(new_words)