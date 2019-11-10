original_word = 'length'
target_word = 'kitchen'


def save_to_csv(edit_matrix, path_to_file):
    path_to_file = open('data.csv', 'w')
    k = 0
    for i in edit_matrix:
        for j in edit_matrix[k]:
            path_to_file.write(j)
            k += 1
    path_to_file.close()


def generate_edit_matrix(num_rows, num_cols):
    edit_matrix = []
    if num_cols is not None and num_rows is not None and type(num_rows) is int and type(num_cols) is int:
        if num_rows != 0 and num_cols != 0:
            edit_matrix = [[0 for j in range(num_cols)] for i in range(num_rows)]
        else:
            return edit_matrix
    else:
        return edit_matrix
    return edit_matrix


def initialize_edit_matrix(edit_matrix, insert_weight, remove_weight):
    edit_matrix = list(edit_matrix)
    k = 0
    m = 0
    if remove_weight is not None and insert_weight is not None and type(remove_weight) is int and type(insert_weight) is int:
        if edit_matrix != []:
            for i in edit_matrix:
                if edit_matrix[0] != []:
                    edit_matrix[0][0] = 0
                    edit_matrix[k][0] = edit_matrix[k-1][0] + remove_weight
                    k += 1
                else:
                    return edit_matrix
            for j in edit_matrix[0]:
                edit_matrix[0][0] = 0
                edit_matrix[0][m] = edit_matrix[0][m - 1] + insert_weight
                m += 1
        else:
            return edit_matrix
    else:
        return edit_matrix
    return edit_matrix


def minimum_value(numbers):
    min1 = 32000
    for i in numbers:
        if i < min1:
            min1 = i
    return min1


def fill_edit_matrix(edit_matrix, insert_weight, remove_weight, substitute_weight, original_word, target_word):
    edit_matrix = list(edit_matrix)
    a, b, c = 0, 0, 0
    if target_word is not None and original_word is not None and edit_matrix != [] and edit_matrix[0] != [] and type(insert_weight) is int and type(remove_weight) is int and type(substitute_weight) is int:
        for i in range(1, len(edit_matrix)):
            for j in range(1, len(edit_matrix[i])):
                a = edit_matrix[i - 1][j] + remove_weight
                b = edit_matrix[i][j - 1] + insert_weight
                if original_word[i - 1] != target_word[j - 1]:
                    c = edit_matrix[i - 1][j - 1] + substitute_weight
                else:
                    c = edit_matrix[i - 1][j - 1]
                numbers = (a, b, c)
                edit_matrix[i][j] = minimum_value(numbers)
        for i in edit_matrix:
            print(i)
        return edit_matrix
    else:
        return edit_matrix


def find_distance(original_word, target_word, insert_weight, remove_weight, substitute_weight):
    if type(original_word) is str and type(target_word) is str and insert_weight is not None and remove_weight is not None and substitute_weight is not None and type(insert_weight) is int and type(remove_weight) is int and type(substitute_weight) is int:

        num_rows = (len(original_word) + 1)
        num_cols = (len(target_word) + 1)
        edit_matrix = generate_edit_matrix(num_rows, num_cols)
        path_to_file = open('data.csv', 'w')
        save_to_csv(edit_matrix, path_to_file)
        initialize_edit_matrix(edit_matrix, insert_weight, remove_weight)
        fill_edit_matrix(edit_matrix, insert_weight, remove_weight, substitute_weight, original_word, target_word)
        print(edit_matrix[num_rows - 1][num_cols - 1])
        return edit_matrix[num_rows - 1][num_cols - 1]
    else:
        return -1


find_distance(original_word, target_word, 1, 1, 2)









