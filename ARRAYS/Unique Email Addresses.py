from ast import List

# METHOD 1: USING BUILT-IN FUNCTION


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for wrd in emails:
            # If entry is not empty
            if len(wrd) > 0:

                # Split entry into two parts - before and after @ sign
                a, b = wrd.split('@')[0], wrd.split('@')[1]

                # If first part (local) contains + sign
                if '+' in a:
                    # Split this part again into two parts - before and after + sign
                    # and replace dots in the first part with nothing, i.e. remove them
                    # then reconstruct mail address by adding @ and the second part
                    res.add(a.split('+')[0].replace('.', '') + '@' + b)

                else:
                    # If there is no + sign in the first part, then only remove dots
                    # and reconstruct mail address by adding @ and the second part
                    res.add(a.replace('.', '') + '@' + b)

        return len(res)


# METHOD 2:
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for wrd in emails:
            # build the local name
            i, local = 0, ""
            while wrd[i] not in ['+', '@']:
                if wrd[i] != '.':
                    local += wrd[i]
                i += 1

            # iterte till i reaches @
            while wrd[i] != '@':
                i += 1

            # building domain name
            domain = wrd[i+1:]
            res.add((local + '@' + domain))
        return len(res)
