my_file = open("samplePuzzles.txt", 'r')

input = []
for line in my_file:
  stripped_line = line.strip()
  input.append(stripped_line)
my_file.close()


print(input)
