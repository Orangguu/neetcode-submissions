class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            encoded_s = str(len(s))
            encoded_s += "#"
            encoded_s += s
            res += encoded_s

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        str_list = []
        str_len = ""

        while i < len(s):

            if s[i] != "#":
                str_len += s[i]
                i += 1

            else:
                i += 1

                idx_of_string_end = int(str_len) + i
                string = ""

                while i < idx_of_string_end:
                    string += s[i]
                    i += 1

                str_list.append(string)

                str_len = ""

        return str_list