import getpass
import sys
import hashlib
import secrets

def passhash(prompt:str, hash_type="sha256", hash_strength=3):
    if hash_type == "sha256":
        hash = ""
        for _ in range(hash_strength):
            hash = hashlib.sha256(bytes(prompt, "utf-8")).hexdigest()

    elif hash_type == "sha1":
        hash = ""
        for _ in range(hash_strength):
            hash = hashlib.sha1(bytes(prompt, "utf-8")).hexdigest()

    elif hash_type == "sha224":
        hash = ""
        for _ in range(hash_strength):
            hash = hashlib.sha224(bytes(prompt, "utf-8")).hexdigest()

    elif hash_type == "sha384":
        hash = ""
        for _ in range(hash_strength):
            hash = hashlib.sha384(bytes(prompt, "utf-8")).hexdigest()

    elif hash_type == "sha512":
        hash = ""
        for _ in range(hash_strength):
            hash = hashlib.sha512(bytes(prompt, "utf-8")).hexdigest()

    elif hash_type == "md5":
        hash = prompt
        for _ in range(hash_strength):
            hash = hashlib.md5(bytes(hash, "utf-8")).hexdigest()

    return hash


def passask(prompt:str="password: ", do_hash:bool=True, hashtype="sha256", hashstrength:bool=3):
    if not sys.stdin.isatty():
        password = input(prompt)

        if do_hash == True:
            password = passhash(password, hash_type=hashtype, hash_strength=hashstrength)

    else:
        password = getpass.getpass(prompt)

        if do_hash == True:
            password = passhash(password, hash_type=hashtype, hash_strength=hashstrength)

    return password

def passgen(length: int = 10, caplock="mix"):
    # Define the letter, numbers and symbols
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
               "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    symbols = ["@", "#", "%", "!", "*", ">", "<", "$"]

    # Check if length parameter is valid
    if length < 1:
        raise ValueError("Length is too short. It has to be greater than 0")

    # Create generator instance
    generartor = secrets.SystemRandom()

    # Create the random string
    result = ""
    turn = "letter"
    for _ in range(length):
        if turn == "letter":
            result += generartor.choice(letters)

            if caplock == True:
                result = result.upper()
            elif caplock == False:
                result = result.lower()

            turn = "number"

        elif turn == "number":
            result += str(generartor.randint(0, 11))
            turn = "symbol"

        elif turn == "symbol":
            result += generartor.choice(symbols)
            turn = "letter"

    # Shuffle the randomized string
    result = list(result)  # generator.shuffle() takes a list, not str
    for _ in range(10):
        generartor.shuffle(result)

    # Join the result back
    final_result = ""
    for i in result:
        final_result += i

    # Return the result
    return final_result
