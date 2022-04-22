from collections import deque

# # Get first input for N and M
# my_in = input()
# number_rows = int(my_in.split(" ")[0])
# letters_per_row = int(my_in.split(" ")[1])

# # Create grid and arrays from inputs
# grid={}
# letter_list = []
# coordinate_list = []
# word_count =0
# for i in range(number_rows):
#     a = input()
#     a = [char for char in a]
#     for j in range(len(a)):
#         temp_grid = {}
#         temp_grid["x"]=j
#         temp_grid["y"]=i
#         temp_grid["letter"]=a[j]
#         grid[word_count]=temp_grid
#         coordinate_list.append([i,j])
#         letter_list.append(a[j])
#         word_count=word_count+1
# # print(grid, letter_list, coordinate_list)

# # Get inputs for wrap and search words
# wrap_or_not = input()
# number_inputs = int(input())
# p = []
# for i in range(number_inputs):
#     a = input()
#     p.append(a)

# answer = []
# answers_as_coordinates = []
# for i in range(len(p)):
#     answer.append([])
#     answers_as_coordinates.append([])



## Hardcoded values for testing
number_rows =3
letters_per_row=3
grid={0: {'x': 0, 'y': 0, 'letter': 'a'}, 1: {'x': 1, 'y': 0, 'letter': 'b'}, 2: {'x': 2, 'y': 0, 'letter': 'c'}, 3: {'x': 0, 'y': 1, 'letter': 'd'}, 4: {'x': 1, 'y': 1, 'letter': 'e'}, 5: {'x': 2, 'y': 1, 'letter': 'f'}, 6: {'x': 0, 'y': 2, 'letter': 'g'}, 7: {'x': 1, 'y': 2, 'letter': 'h'}, 8: {'x': 2, 'y': 2, 'letter': 'i'}}
wrap_or_not = "NO_WRAP"
p = ["fed",
"cab",
"gad",
"bid",
"high",]

letter_list = []
coordinate_list = []
for val in range(len(grid)):
    letter_list.append(grid[val]["letter"])
    coordinate_list.append([grid[val]["y"], grid[val]["x"]])

answer =  [[],[],[], [], []]
answers_as_coordinates = [[],[],[], [], []]


# Create neighbors list
neighbors_grid = []

for item in grid:
    temp_grid_neighbors = []
    x = grid[item]["x"]
    y = grid[item]["y"]
    if wrap_or_not == "WRAP":
        new_x = [x-1, x, x+1]
        new_y = [y-1,y,y+1]
    elif wrap_or_not == "NO_WRAP":
        if x == 0:
            new_x = [0, 1]
        elif x == letters_per_row-1:
            new_x = [x, x-1]
        else:
            new_x = [x-1, x, x+1]
        if y == 0:
            new_y = [0, 1]
        elif y == number_rows-1:
            new_y = [y, y-1]
        else:
            new_y = [y-1,y,y+1]
    for k in new_x:
        for l in new_y:
            if not (k == x and l ==y):
                temp_grid_neighbors.append([k,l])
    # print("grid neighbors", temp_grid_neighbors)

    new_keys = []
  
    for val in temp_grid_neighbors:
        if val[0]>=0 and val[0]<letters_per_row:
            x = val[0]
        else:
            x = val[0] % letters_per_row
        if val[1]>=0 and val[1]<number_rows:
            y = val[1]
        else:
            y = val[1] % number_rows
        position = coordinate_list.index([y,x])
        new_keys.append(position)
        # print("postion",position,"new keys", new_keys)
    neighbors_grid.append(new_keys)

# print("neighbors_grid",neighbors_grid)

# Find matches for each word 
for i in range(len(p)):
    word = p[i]
    first_letter = word[0]
    word_length = len(word)
    q = deque()
    for x in grid:
        if grid[x]["letter"]==first_letter:
            temp_dict = {"square":x, "seed_list":[x] }
            q.append(temp_dict)

    while q:
        print("q", q)
        x = q.popleft()
        working_list = x["seed_list"]
        target_square = x["seed_list"][-1]
        temp_queue = deque()
        my_length = len(x["seed_list"])

        if my_length == word_length:
            answer[i].append(working_list)
            break

        next_letter = word[my_length]

        for val in neighbors_grid[target_square]:
            if letter_list[val] == next_letter and val not in working_list:
                temp_dict={"square":val, "seed_list":working_list+[val]}
                temp_queue.append(temp_dict)
                print("working list", working_list, "temp queue", temp_queue)
                print(" ")

        while temp_queue:
            y = temp_queue.pop()
            q.appendleft(y)
     
        

# Construct and report answer in corrent format
for u in range(len(answer)):
    for v in range(len(answer[u])):
        answers_as_coordinates[u].append([
        coordinate_list[answer[u][v][0]], 
        coordinate_list[answer[u][v][-1]]
        ])


for u in range(len(answers_as_coordinates)):
    if not answers_as_coordinates[u]:
        print("not found")
    else: 
        print(answers_as_coordinates[u])


