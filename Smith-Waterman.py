#Sequences
sequence_1 = "GGTTGACTA"
sequence_2 = "TGTTACGG"
split_1 = list(sequence_1)
split_2 = list(sequence_2)
len_1 = len(split_1)+1
len_2 = len(split_2)+1

#Scoring system
match = 3
mismatch = -3
gap = -2 #Linear gap penalty

#Constructing the matrices and setting them to zero.
#matrix will contain the scores
matrix = []
for x in range(len_1):
    matrix.append([0]*len_2)

#pointers  will contain the arrows
pointers = []
for x in range(len_1):
    pointers.append([0]*len_2)

#Filling the scoring matrix. Score cannot be negative, so negative score is set to zero.
for i in range(1, len_1):
    for j in range(1,len_2):
        if split_1[i-1] == split_2[j-1]:
            value1 = matrix[i-1][j-1] + match
            if value1 < 0:
                value1 = 0
        else:
            value1 = matrix[i-1][j-1] + mismatch
            if value1 < 0:
                value1 = 0
        value2 = matrix[i-1][j] + gap
        if value2 < 0:
                value2 = 0
        value3 = matrix[i][j-1] + gap
        if value3 < 0:
                value3 = 0
        matrix[i][j] = max(value1, value2, value3)
        #Filling the pointers matrix
        if matrix[i][j] == 0:
            pointers[i][j] = 0
        elif matrix[i][j] == value1:
            pointers[i][j] = "D"
        elif matrix[i][j] == value2:
            pointers[i][j] = "U"
        elif matrix[i][j] == value3:
            pointers[i][j] = "L"
   
#Score of the best alignment, corresponding to cell with the highest score
def max_val(lists):
    max_value = 0
    for i in range(len(lists)):
        for j in range(len(lists[0])):
            if lists[i][j] > max_value:
                max_value = lists[i][j]
                x = i
                y = j
    return max_value, x, y
score = max_val(matrix)[0]

print("The score of the optimal alignment is ",score)

#Traceback. Choosing elements from Seq1, Seq2 or Seq1 and Seq2
#depenging on the arrow in the pointers matrix
i = max_val(matrix)[1]
j = max_val(matrix)[2]

alignment_1 = ""
alignment_2 = ""
while pointers[i][j] != 0:
    if pointers[i][j] == "D":
        alignment_1 = split_1[i-1] + alignment_1
        alignment_2 = split_2[j-1] + alignment_2
        i = i - 1
        j = j - 1
    elif pointers[i][j] == "L":
        alignment_1 = "-" + alignment_1
        alignment_2 = split_2[j-1] + alignment_2
        j = j-1
    elif pointers[i][j] == "U":
        alignment_1 = split_1[i-1] + alignment_1
        alignment_2 = "-" + alignment_2
        i = i-1

#Function to print the marices
def print_matrix(matrix):
    for s in matrix:
        print(*s)
    return " "

print(print_matrix(matrix))
print(print_matrix(pointers))
print(alignment_1)
print(alignment_2)
