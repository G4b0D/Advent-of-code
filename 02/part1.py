COLORS = ["red","green","blue"]
ans = 0
def possible_games(game_sets_values: dict,input_values: list[int]) -> list[int]:
    r,g,b = input_values[0],input_values[1],input_values[2]
    possible_red = [i+1 for i,val in enumerate(game_sets_values["red"]) if val <= r]
    possible_green = [i+1 for i,val in enumerate(game_sets_values["green"]) if val <= g]
    possible_blue = [i+1 for i,val in enumerate(game_sets_values["blue"]) if val <= b]
    possible_games = list(set(possible_blue) & set(possible_green) & set(possible_red))
    return possible_games
    

max_values = {"red":[],"green":[],"blue":[]}
with open("./input2.txt","r") as input:
    for game in [l.strip() for l in input ]:
        sets = game.split(": ")[1].split("; ")
        game_max_value = {"red":0,"green":0,"blue":0}
        for game_set in sets:
            s = game_set.split(", ")
            if len(s) > 1:
                for color in COLORS:
                    ci = next((i for i,e in enumerate(s) if color in e),None)
                    if ci is not None:
                        game_max_value[color] = int(s[ci].replace(f" {color}","")) if int(s[ci].replace(f" {color}","")) > game_max_value[color] else game_max_value[color]
            else:
                for color in COLORS:
                    if color in s[0]:
                        game_max_value[color] = int(s[0].replace(f" {color}","")) if int(s[0].replace(f" {color}","")) > game_max_value[color] else game_max_value[color]
        max_values["blue"].append(game_max_value["blue"])
        max_values["green"].append(game_max_value["green"])
        max_values["red"].append(game_max_value["red"])
pg = possible_games(max_values,[12,13,14])
for p in pg:
    ans += p
print(ans)
#print(max_values)
