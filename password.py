import secrets
def create_new(lenth, characters):
    return "".join(secrets.choice(characters) for _ in range(lenth))