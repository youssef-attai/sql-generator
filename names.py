import json
import random
import enum

class NameType(enum.Enum):
    MALE = 1
    FEMALE = 2
    LAST = 3

names = dict()

# Load the names from the json files
with open("male-names.json", "r") as f:
    names[NameType.MALE] = json.loads(f.read())["names"]

with open("female-names.json", "r") as f:
    names[NameType.FEMALE] = json.loads(f.read())["names"]

with open("last-names.json", "r") as f:
    names[NameType.LAST] = json.loads(f.read())["names"]

def generate_random_name(gender: NameType, length: int):
    assert gender == NameType.MALE or gender == NameType.FEMALE, "Invalid gender"

    if length <= 0:
        return ""

    name = random.choice(names[gender]) + " "

    for _ in range(length - 2):
        name += random.choice(names[gender]) + " "

    if length > 1:
        name += random.choice(names[NameType.LAST])
    else:
        name = name[:-1]

    return name


def generate_random_female_name(length: int):
    return generate_random_name(NameType.FEMALE, length)


def generate_random_male_name(length: int):
    return generate_random_name(NameType.MALE, length)


if __name__ == "__main__":
    print(generate_random_name(NameType.MALE, 3))
