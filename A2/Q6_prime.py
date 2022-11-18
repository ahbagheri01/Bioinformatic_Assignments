import numpy as np

f = open("test2.txt","w")
def print_alignment(b, dna_strings_a, dna_strings, i, j, k, l):
    while i > 0 or j > 0 or k > 0 or l > 0:
        order = b[i, j, k, l]
        dna_strings_a[0].append(dna_strings[0][i - 1] if order[0] else '-')
        dna_strings_a[1].append(dna_strings[1][j - 1] if order[1] else '-')
        dna_strings_a[2].append(dna_strings[2][k - 1] if order[2] else '-')
        dna_strings_a[3].append(dna_strings[3][l - 1] if order[3] else '-')
        i, j, k, l = i - order[0], j - order[1], k - order[2], l - order[3]


Orders = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
          [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0],
          [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]

if __name__ == '__main__':
    input_file = open("rosalind_mult.txt", "r")
    current_string = ''
    dna_strings = []
    for line in input_file.readlines():
        if line.startswith('>'):
            if current_string != '':
                dna_strings.append(current_string)
            current_string = ''
        else:
            current_string += line.rstrip()
    dna_strings.append(current_string)

    dp = np.zeros((len(dna_strings[0]) + 1, len(dna_strings[1]) + 1, len(dna_strings[2]) + 1, len(dna_strings[3]) + 1))
    b = [[[[None for l in range(len(dna_strings[3]) + 1)] for k in range(len(dna_strings[2]) + 1)] for j in
          range(len(dna_strings[1]) + 1)] for i in range(len(dna_strings[0]) + 1)]
    b = np.asarray(b)
    for i in range(1, len(dna_strings[0]) + 1):
        dp[i, 0, 0, 0] = -i * 3
        b[i, 0, 0, 0] = [1, 0, 0, 0]
    for i in range(1, len(dna_strings[1]) + 1):
        dp[0, i, 0, 0] = -i * 3
        b[0, i, 0, 0] = [0, 1, 0, 0]
    for i in range(1, len(dna_strings[2]) + 1):
        dp[0, 0, i, 0] = -i * 3
        b[0, 0, i, 0] = [0, 0, 1, 0]
    for i in range(1, len(dna_strings[3]) + 1):
        dp[0, 0, 0, i] = -i * 3
        b[0, 0, 0, i] = [0, 0, 0, 1]
    

    for i in range(len(dna_strings[0]) + 1):
        for j in range(len(dna_strings[1]) + 1):
            for k in range(len(dna_strings[2]) + 1):
                for l in range(len(dna_strings[3]) + 1):
                    if i + j + k + l > 1:
                        best_score = -np.inf
                        best_order = None
                        for order in Orders:
                            if (not order[0] or i > 0) and (not order[1] or j > 0) and (not order[2] or k > 0) and (
                                    not order[3] or l > 0):
                                f.write(f"{(i,j,k,l)}\n")
                                s0_o = dna_strings[0][i - 1] if order[0] else '-'
                                s1_o = dna_strings[1][j - 1] if order[1] else '-'
                                s2_o = dna_strings[2][k - 1] if order[2] else '-'
                                s3_o = dna_strings[3][l - 1] if order[3] else '-'
                                strings = [s0_o, s1_o, s2_o, s3_o]
                                score = dp[i - order[0]][j - order[1]][k - order[2]][l - order[3]]
                                #f.write(f"{score} {(i,j,k,l)}\n")
                                for o0 in range(len(strings) - 1):
                                    for o1 in range(o0 + 1, len(strings)):
                                        score += 0 if strings[o0] == strings[o1] else -1
                                if score > best_score:
                                    best_score = score
                                    best_order = order

                        dp[i, j, k, l] = best_score
                        b[i, j, k, l] = best_order

    dna_strings_a = [[], [], [], []]
    print_alignment(b, dna_strings_a, dna_strings, len(dna_strings[0]), len(dna_strings[1]), len(dna_strings[2]),
                    len(dna_strings[3]))

    print(int(dp[len(dna_strings[0]), len(dna_strings[1]), len(dna_strings[2]), len(dna_strings[3])]))
    print(''.join(reversed(dna_strings_a[0])))
    print(''.join(reversed(dna_strings_a[1])))
    print(''.join(reversed(dna_strings_a[2])))
    print(''.join(reversed(dna_strings_a[3])))