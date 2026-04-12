def on_every_line(word:str, filename:str):
    with open(filename, "r") as file:
        for line in file:
            on_line = False 
            values = line.split()
            for val in values:
                if val == word:
                    on_line = True # if the word appears then on_line returns true 
            if word not in values:
                return False
    return True

def most_common_word(sentence:str):
    common_dict = {}
    sentence_list = sentence.split()
    max_apperances = 0
    max_word = ""
    for word in sentence_list:
        if word not in common_dict.keys(): # this accesses the key in the dictionary .keys() searches throught the keys
            common_dict[word] = 1
        else:
            common_dict[word] += 1
        if common_dict[word] > max_apperances: # it wont be a = to return the first most common word  To get the last most common word
            # we can use >= so it becomes the last most common word
            max_apperances = common_dict[word]
            max_word = word
    return max_word

def sum_of_each_row(matrix: list[list]):
    sum_list = []
    for row in range(len(matrix)):
        sum = 0
        for col in range(len(matrix[row])):
            sum += matrix[row][col] # index through the row then the column instead of [col][row] 
        sum_list.append(sum)
    return sum_list

def smallest_each(li: list[tuple[str, int]]) -> list[tuple[str, int]]:
    smallest_dict = {}
    list = []
    for pair in li:
        if pair[0] not in smallest_dict.keys():
            smallest_dict[pair[0]] = pair[1]
        elif pair[1] < smallest_dict[pair[0]]:
            smallest_dict[pair[0]] = pair[1]
    for items in smallest_dict.keys():# calls each item by the key name 
        list.append((items, smallest_dict[items]))   
    return list

def what_ranking(fighter_name:str, ranking_file:str):
    with open(ranking_file, "r") as file:
        for line in file:
            parts = line.split()
                #[1:] will go to the end of the list 
            if  parts[1:] == fighter_name.split():
                return f"{fighter_name} is ranked number {parts[0]}"
    return "fighter is not ranked in pound for pound list"

def largest_on_each_row(matrix: list[list]):
    largest_list = []
    for row in range(len(matrix)):
        largest = None
        for col in range(len(matrix[row])):
            if largest is None or matrix[row][col] > largest:
                largest = matrix[row][col]
        largest_list.append(largest) # this only wants the one largest at the end of each row 
        # the loop would nest under the for loop 
        
    return largest_list



