
def max_num(n: int) -> int:
    """Given an integer N, return maximum number after deleting one '5'. N will contian at least one '5'."""
    digits = []
    positive = False

    idx = 0
    skipped_idx = -1
    if n > 0:
        positive = True
        first_5 = True
        prev_digit = 1000000

        while n > 0:
            cur_digit = n % 10
            if cur_digit == 5 and (prev_digit > 5 or first_5):
                first_5 = False
                skipped_idx = idx
            digits.append(cur_digit)
            n //= 10
            idx += 1
            prev_digit = cur_digit
    else:
        prev_digit = -1000000
        n = n * -1
        first_5 = True
        while n > 0:
            cur_digit = n % 10
            if cur_digit == 5 and (prev_digit < 5 or first_5):
                first_5 = True
                skipped_idx = idx
            digits.append(cur_digit)
            n //= 10
            idx += 1
            prev_digit = cur_digit

    skipped_idx = len(digits) - 1 - skipped_idx
    for idx, cur_digit in enumerate(reversed(digits)):
        if idx == skipped_idx:
            continue
        n = 10 * n + cur_digit

    return n if positive else -n
