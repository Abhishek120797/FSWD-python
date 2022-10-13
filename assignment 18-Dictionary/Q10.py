sample_dict = {'C': 92,'Java': 66,'Python': 85}
temp=sample_dict["C"]
for e in sample_dict:
    if sample_dict[e]<temp:
        temp=sample_dict[e]
for e in sample_dict:
    if sample_dict[e]==temp:
        print(e, "is key of minimum value")
