"""Sub-string problems."""
from typing import List


def substring_replace(main_str: str, sub_str: str) -> str:
    """Insert a pair of parenthesis in each substring found in the main string."""
    res_str: List[str] = []
    i = 0
    k = 0
    for j in range(len(main_str)):
        if main_str[j] == sub_str[k]:
            k += 1
        else:
            res_str.extend(main_str[i : j + 1])
            i = j + 1
            k = 0

        if k == len(sub_str):
            res_str.append("(")
            res_str.extend(main_str[i : j + 1])
            res_str.append(")")
            k = 0
            i = j + 1
    return "".join(res_str)


if __name__ == "__main__":
    # s1 = "sust cse is a cse dept."
    # s2 = "cse"
    # assert substring_replace(main_str=s1, sub_str=s2) == "sust (cse) is a (cse) dept."

    s1 = "abdefabcdef"
    s2 = "abc"
    assert substring_replace(main_str=s1, sub_str=s2) == "abdef(abc)def"
