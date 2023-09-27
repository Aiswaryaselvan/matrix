# Defining matrix dimensions
n = 4                     # rows
m = 5                   # columns
matrix1 = [
    "1 @ 2 % 3 !",
    "A   B C D E",
    "x y z1  ",
    "4 5 6"
]

result= ""

for i in range(m):
    word = ""
    for j in range(n):
        character = matrix1[j] [i]
        if character.isalnum() or (word and character == ' '):
            word =word+ character
    result =result+ word + ' '

print(result.replace('  ', ' ').rstrip())  # it removes additional spaces and give result
