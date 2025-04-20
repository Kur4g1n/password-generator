import random
from argparse import ArgumentParser

DIGITS = tuple("1234567890")


def generate(length: int) -> str:
    return "".join([random.choice(DIGITS) for _ in range(length)])


if __name__ == "__main__":
    parser = ArgumentParser(description="Generates password of given lenght")
    parser.add_argument(
        "length",
        type=int,
        help="Length of the password to be generated",
    )
    parser.add_argument(
        "--passwords",
        "-p",
        type=int,
        help="Number of passwords to generate",
        required=False,
        default=1,
    )
    args = parser.parse_args()
    n_passwords = args.passwords
    if n_passwords == 1:
        print(f"Password: {generate(args.length)}")
    elif n_passwords > 1:
        print(
            "Passwords:\n"
            f"{"\n".join([f"{i+1} {generate(args.length)}" for i in range(n_passwords)])}"
        )
    else:
        print("No passwords to generate")
