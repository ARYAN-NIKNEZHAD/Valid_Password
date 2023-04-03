import string
import argparse

from random import choices


def create_password(length=8, upper=False, lower=False, digit=False, pun=False):
    pool = ""

    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits
    if pun:
        pool += string.punctuation
    if pool == "":
        pool = string.ascii_letters

    return "".join(choices(pool, k=length))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int, help="Length of password")
    parser.add_argument(
        "-l", "--lower", help="User Lower case", action="store_true"
    )
    parser.add_argument(
        "-u", "--upper", help="User Upper case", action="store_true"
    )
    parser.add_argument(
        "-d", "--digit", help="User Lower case", action="store_true"
    )
    parser.add_argument(
        "-p", "--pun", help="User pun", action="store_true"
    )

    args = parser.parse_args()
    print(args.length)
    print(create_password(
        args.length, args.upper, args.lower, args.digit, args.pun
    ))

    # print(create_password(upper=True))
