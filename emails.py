import random

domains = [
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "aol.com",
    "protonmail.com",
    "icloud.com",
    "zoho.com",
    "mail.com",
    "yandex.com",
    "inbox.com"
]

separators = ["_", ".", ""]


def generate_random_email(name):
    domain = random.choice(domains)
    names = name.lower().replace("'", "").split(" ")
    for i in range(len(names)):
        if random.randint(0, 1) == 1:
            names[i] = names[i] + str(random.randint(0, 100))
    for i in range(len(names) - 1):
        names[i] = names[i] + random.choice(separators)
    return f"{''.join(names)}@{domain}"


if __name__ == "__main__":
    print(generate_random_email("John Doe"))
