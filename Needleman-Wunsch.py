#Sequences
sequence_1 = "ATCGT"
sequence_2 = "TGGTG"
split_1 = list(sequence_1)
split_2 = list(sequence_2)
len_1 = len(split_1)+1
len_2 = len(split_2)+1

#Scoring system
match = 1
mismatch = -1
gap = -2

#Constructing the matrices
#matrix will contain the scores
matrix = []
for x in range(len_1):
    matrix.append([0]*len_2)

#pointers  will contain the arrows
pointers = []
for x in range(len_1):
    pointers.append([0]*len_2)
                    
#Initialization. Filling the (i,0) y (0,j) positions with gap's score and arrows
# "U" = UP
# "L" = LEFT
# "D" = DIAGONAL
for i in range(len_1):
    matrix[i][0]= gap * i
    pointers[i][0] = "U"
for j in range(len_2):
    matrix[0][j]= gap*j
    pointers[0][j] = "L"
pointers[0][0] = "0"

#Filling the scoring matrix
for i in range(1, len_1):
    for j in range(1,len_2):
        if split_1[i-1] == split_2[j-1]:
            value1 = matrix[i-1][j-1] + match
        else:
            value1 = matrix[i-1][j-1] + mismatch
        value2 = matrix[i-1][j] + gap
        value3 = matrix[i][j-1] + gap
        matrix[i][j] = max(value1, value2, value3)
        #Filling the pointers matrix
        if matrix[i][j] == value1:
            pointers[i][j] = "D"
        elif matrix[i][j] == value2:
            pointers[i][j] = "U"
        elif matrix[i][j] == value3:
            pointers[i][j] = "L"
    
#Score of the best alignment, corresponding to the bottom right cell
score = matrix[-1][-1]
print("The score of the optimal alignment is ",score)

#Traceback. Choosing elements from Seq1, Seq2 or Seq1 and Seq2
#depending on the arrow in the pointers matrix
i = len(sequence_1)-1
j = len(sequence_2)-1
alignment_1 = ""
alignment_2 = ""
while (i != -1) or (j != -1):
    if pointers[i+1][j+1] == "D":
        alignment_1 = split_1[i] + alignment_1
        alignment_2 = split_2[j] + alignment_2
        i = i - 1
        j = j - 1
    elif pointers[i+1][j+1] == "L":
        alignment_1 = "-" + alignment_1
        alignment_2 = split_2[j] + alignment_2
        j = j-1
    elif pointers[i+1][j+1] == "U":
        alignment_1 = split_1[i] + alignment_1
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
