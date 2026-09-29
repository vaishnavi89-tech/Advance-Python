
def lcs(text1, text2):

    rows = len(text1)
    columns = len(text2)

    table = [[0 for column in range(columns + 1)]
             for row in range(rows + 1)]

    for row in range(1, rows + 1):
        for column in range(1, columns + 1):

            if text1[row - 1] == text2[column - 1]:
                table[row][column] = table[row - 1][column - 1] + 1

            else:
                table[row][column] = max(
                    table[row - 1][column],
                    table[row][column - 1]
                )

    common_length = table[rows][columns]

    row = rows
    column = columns
    answer = []

    while row > 0 and column > 0:

        if text1[row - 1] == text2[column - 1]:
            answer.append(text1[row - 1])
            row -= 1
            column -= 1

        elif table[row - 1][column] > table[row][column - 1]:
            row -= 1

        else:
            column -= 1

    answer.reverse()

    return common_length, ''.join(answer)


text1 = input("Enter first sequence: ")
text2 = input("Enter second sequence: ")

final_length, final_sequence = lcs(text1, text2)

print("\nLongest Common Subsequence:", final_sequence)
print("Length of LCS:", final_length)

