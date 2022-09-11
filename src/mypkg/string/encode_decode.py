"""Strings encoder and decoder."""
from typing import List


class Codec:
    """Strings encoder and decoder."""

    SEPARATOR = ":"

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        return "".join(f"%d{Codec.SEPARATOR}%s" % (len(s), s) for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        idx = 0
        strs: List[str] = []

        while idx < len(s):
            sep_idx = s.find(Codec.SEPARATOR, idx)
            s_len = int(s[idx:sep_idx])
            idx = sep_idx + 1 + s_len
            strs.append(s[sep_idx + 1 : idx])

        return strs


if __name__ == "__main__":
    codec = Codec()
    strs = ["Hello", "World", "This is cse", "from sust."]
    e_str = codec.encode(strs)
    print(f"Encoded: {e_str}, type={type(e_str)}")
    d_str = codec.decode(e_str)
    print(f"Decoded: {d_str}, type={type(d_str)}")
    assert d_str == strs
