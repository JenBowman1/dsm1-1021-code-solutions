record = (1, 'Grimdiana', 'Bones', 'boulders')
row = ''
for x in record:
  row = row + str(x) + ","
print(row)

values_list = [1, 1, 2, 3, 5]
for x in values_list:
  print(x)

index_list = []
for idx,  val in enumerate(values_list):
  index_list.insert(0, idx)
print(index_list)

for idx, val in enumerate(index_list):
  if val % 2 != 0:
    values_list.remove(values_list[idx])
print(values_list)


vowels = {"A", "E", "I", "O", "U"}

parts_of_the_big_letter = {"L", "M", "N", "O", "P"}

for x in vowels:
  parts_of_the_big_letter.discard(x)
print(parts_of_the_big_letter)

player_positions = {
    "Who": "1B",
    "What": "2B",
    "I Don't Know": "3B",
    "Why": "LF",
    "Because": "CF",
    "Tomorrow": "P",
    "Today": "C",
    "I Don't Care": "SS"
}

players = []
for x in player_positions.keys():
  players.append(x)
print(players)

positions = []
for x in player_positions.values():
  positions.append(x)
print(positions)

for key, value in player_positions.items():
  print(key + " is on " + value)
