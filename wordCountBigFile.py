f = open("Big file text.rtf", "r")
data =f.read()
f.close()

words = data.split(" ")
num_words = len(words)
print("The number of words is ", num_words)