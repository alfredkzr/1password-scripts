import subprocess
import os

#Run this command in your terminal to sign in to 1Password 1st
#command = "eval $(op signin) -f --account your1pwenterprise"
#os.system(command)

with open("1password-scripts/users.txt") as f: #ensure users.txt filepath is correct
    names = f.read().strip().split("\n")

for name in names:
    get_user_command = f"op user get {name}"
    print(get_user_command)
    os.system(get_user_command)
    