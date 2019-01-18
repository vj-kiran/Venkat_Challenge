import re
for _ in range(int(input())):
    credit_card = input()
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", credit_card) and not re.search(r"([\d])\1\1\1", credit_card.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")