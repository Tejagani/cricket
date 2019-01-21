import re

st = "LCNO-TND-10-10-990"

res = re.search(r'LCNO-(KAR|KER|TND|MAH|APN|TLN|GOA)-([0-6][1-9]|[1-7][0-3])-([0-9][1-9]|[1-9]0)-([0-9]{2}[1-9]|[0-9][1-9][0-9][1-9][0-9]{2})', st)

print("res :", res)


if res:
    print("match found...")
    print(res.group())
else:
    print("Match not found...")