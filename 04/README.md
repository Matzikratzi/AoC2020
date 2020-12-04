# emacs fix of input

ok, I found this a bit hard, so I made the input a bit easier to parse
by putting all fields for a passport on the same line.

A few search and replaces later, the input was like this:

iyr:1928 cid:150 pid:476113241 eyr:2039 hcl:a5ac0f ecl:#25f8d2 byr:2027 hgt:190
hgt:168cm eyr:2026 ecl:hzl hcl:#fffffd cid:169 pid:920076943 byr:1929 iyr:2013


hm, I handled all lines as lists, so I could have sorted them as
well. That would have made the first part easier.