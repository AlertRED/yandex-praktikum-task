import string
import difflib

from typing import Dict


def __normalize(text: str) -> str:
    return text.lower().translate(
        str.maketrans('', '', string.punctuation),
    )


def best_key_by_value(
    input_dict: Dict[str, str],
    keyword: str,
    cutoff: int,
) -> str:
    best_key = None
    best_score = 0
    keyword = __normalize(keyword)
    for key, value in input_dict.items():
        value = __normalize(value)
        score = difflib.SequenceMatcher(None, keyword, value).ratio()
        if score >= best_score:
            best_key, best_score = key, score
    return best_key if best_score >= cutoff else None


if __name__ == '__main__':
    dct = {
        'a1': 'это один',
        'a2': 'это два',
    }
    result = best_key_by_value(dct, 'это двас', 0.9)
    assert result == 'a2'
