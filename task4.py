def adding_need_element(str):
    max_length = max(len(s) for s in str)
    new_str=[s.ljust(max_length, '_') for s in str]

    return new_str
ask_str=["Anna","apple","milkas"]
answer_str=adding_need_element(ask_str)
print(answer_str)
