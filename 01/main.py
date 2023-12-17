ans = 0
with open("./input.txt","r") as calibration_book:
    num_names = ["one","two","three","four","five", "six", "seven", "eight","nine"]
    for calibration_string in [l.strip() for l in calibration_book]:
        digits = []
        for i,c in enumerate(calibration_string):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(num_names):
                if calibration_string[i:].startswith(val):
                    digits.append(str(d+1))
        score = int(digits[0]+digits[-1])
        ans += score
print(ans)