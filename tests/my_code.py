import bisect


if __name__ == "__main__":
    s = [1, 0, 0, 1]

    for i in range((len(s) + 1) // 2):
        s[i], s[~i] = s[~i] ^ 1, s[i] ^ 1
    print(s)
