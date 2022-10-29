from pathlib import Path

easy, medium, hard = [], [], []

p = Path("./src")


for file in p.iterdir():
    number, name, difficulty = file.name.split("-")
    if difficulty == "E":
        easy.append([number, name])
    elif difficulty == "M":
        medium.append([number, name])
    else:
        hard.append([number, name])
    

print(f"Easy(counts:{len(easy)})".center(80, "-"))
for item in easy:
    print(f"{item[0]:^6} {item[1]:{chr(12288)}^60}")

print()
print(f"Medium(counts:{len(medium)})".center(80, "-"))
for item in medium:
    print(f"{item[0]:^6} {item[1]:{chr(12288)}^60}")

print()
print(f"Hard(counts:{len(hard)})".center(80, "-"))
for item in hard:
    print(f"{item[0]:^6} {item[1]:{chr(12288)}^60}")