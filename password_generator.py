from enum import IntFlag
import random
from argparse import ArgumentParser

DIGITS = tuple("1234567890")
LETTERS = tuple("qwertyuiopasdfghjklzxcvbnm")
SPECIAL_SYMBOLS = tuple(r"r'.^$*+?{}[]()|\'")


class CharGroup(IntFlag):
    NONE = 0
    DIGITS = 1 << 0
    LETTERS = 1 << 1
    SPECIAL = 1 << 4


def generate(length: int, include_chars: CharGroup) -> str:
    if include_chars == CharGroup.NONE:
        raise ValueError("Need to choose at least one character group")
    available_chars = []
    if CharGroup.DIGITS & include_chars:
        available_chars += list(DIGITS)
    if CharGroup.LETTERS & include_chars:
        available_chars += list(LETTERS)
    if CharGroup.SPECIAL & include_chars:
        available_chars += list(SPECIAL_SYMBOLS)
    return "".join([random.choice(available_chars) for _ in range(length)])


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
    parser.add_argument(
        "-c",
        "--characters",
        type=str,
        help="Sets of characters to use in password generation joined with +.\n"
        "Available sets:\n"
        "digits: 0-9 (default)\n"
        "letters: a-z\n"
        "special: *, #, etc.",
        required=False,
        default="digits",
    )
    args = parser.parse_args()
    groups = list(args.characters.split("+"))
    groups_mask = CharGroup.NONE
    if "digits" in groups:
        groups_mask |= CharGroup.DIGITS
    if "letters" in groups:
        groups_mask |= CharGroup.LETTERS
    if "special" in groups:
        groups_mask |= CharGroup.SPECIAL
    n_passwords = args.passwords
    if n_passwords == 1:
        print(f"Password: {generate(args.length, groups_mask)}")
    elif n_passwords > 1:
        print(
            "Passwords:\n"
            f"{
                "\n".join(
                    [f"{i+1} {generate(args.length, groups_mask)}" for i in range(n_passwords)]
                )
            }"
        )
    else:
        print("No passwords to generate")
        groups_mask += CharGroup.LETTERS
