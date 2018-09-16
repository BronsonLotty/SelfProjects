class rever():
    def reverse(self, str):

        value = int(str)
        if value == 0:
            return 0
        elif value < 0:
            str = str[1:]
            return -int(str[::-1])
        else:
            return int(str[::-1])

str = input().strip()
print(rever().reverse(str))

# import re
# str = []
# ans = input()
# LEN = len(ans)
# if re.match("^[-+]?[0-9]",ans):
#     if re.match("^[-+]",ans[0]):
#         str.append(ans[0])
#         for i in range(LEN-1):
#             str.append(ans[LEN - i - 1])
#     else:
#         for i in range(LEN):
#             str.append(ans[LEN-i-1])
#     print(int("".join(str)))