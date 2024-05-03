from typing import List, Union


def series_sum(incoming: List[Union[str, float]]) -> str:
    result = ''
    for i in incoming:
        result += str(i)
    return result


print(series_sum(['132', 123]))
