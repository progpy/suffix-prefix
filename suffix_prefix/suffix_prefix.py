from collections import defaultdict


def get_words(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def find_suffix_prefix(words):
    prefixes = defaultdict(set)
    for word in words:
        for length in range(1, len(word) + 1):
            prefix = word[:length]
            prefixes[prefix].add(word)

    answer = []
    answer_length = 0
    for word2 in words:
        min_len = answer_length
        max_len = len(word2)
        for length in range(max_len, min_len, -1):
            substr = word2[-length:]
            substr_found = False

            if substr in prefixes:
                for word1 in prefixes[substr]:
                    if word1 != word2:
                        answer_length = length
                        answer = [word1, word2]
                        substr_found = True
                        break

            if substr_found:
                break

    if answer_length:
        return (answer, answer_length)

    return None


if __name__ == '__main__':
    print(find_suffix_prefix(get_words('1.txt')))
