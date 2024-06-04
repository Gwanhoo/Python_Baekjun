import sys

user_input = sys.stdin.readline().strip()

croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alphabet in croatian_alphabets:
    user_input = user_input.replace(alphabet, "*")
    
print(len(user_input))
