# Regex pattern: [,.] means split on comma (,) or dot (.)
regex_pattern = r"[,.]"   # Do not delete 'r'

import re   # Import regex module

# Take input string, split it wherever ',' or '.' appears,
# then join the parts with newline '\n' so each part comes in a new line,
# finally print the result
print("\n".join(re.split(regex_pattern, input())))
