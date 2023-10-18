import subprocess
import os

#Run this command in your terminal to sign in to your 1Password 1st
#eval $(op signin) -f --account your1pwenterprise

with open("1password-scripts/users.txt") as f: #ensure users.txt filepath is correct
    names = f.read().strip().split("\n")

response = input("Are you sure you want to proceed with the suspension? (y/n)")
response2 = input("Have you checked/update the users.txt file? (y/n)")
if response == "y" & response2 == "y":
    for name in names:
        suspend_user = f"op user suspend {name}"
        os.system(suspend_user)
        print(f"Suspending {name}")
else:
    print("Cancelling operation.")