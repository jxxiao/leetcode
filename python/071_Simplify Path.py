class Solution:
    def simplifyPath(self, path: str) -> str:
        str_list = path.split('/')
        out = []
        for str_i in str_list:
            if str_i == '..' and out:
                out.pop()
            elif str_i in set(['', '.']) or (str_i == '..' and not out):
                pass
            else:
                out.append(str_i)
        return '/'+'/'.join(out)
