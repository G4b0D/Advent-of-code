COLORS = ["red","green","blue"]
ans = 0
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
        power = int(game_max_value["blue"]) * int(game_max_value["green"]) * int(game_max_value["red"])
        ans += power
print(ans)