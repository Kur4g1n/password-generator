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
    args = parser.parse_args()
    print(f"Password: {generate(args.length)}")
