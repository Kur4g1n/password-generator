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
    SPECIAL = 1 << 2


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
        groups_mask += CharGroup.DIGITS
    if "letters" in groups:
        groups_mask += CharGroup.LETTERS
    if "special" in groups:
        groups_mask += CharGroup.SPECIAL

    print(f"Password: {generate(args.length, groups_mask)}")
