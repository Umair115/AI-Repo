with open("names.txt","w") as f:
    f.write("Umair\n")
    f.write("Ammar")

with open("names.txt","a") as f:
    f.write("\nAbdullah")

with open("names.txt","r") as f:
    text_of_file = f.read()

print(text_of_file)

