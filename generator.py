import random,string
def generate_password():
 chars=string.ascii_letters+string.digits+string.punctuation
 return "".join(random.choice(chars) for _ in range(16))
