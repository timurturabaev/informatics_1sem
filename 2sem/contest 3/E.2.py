
def is_palindrome(s):
    return s == s[::-1]


def find_palindrome_pairs(words):
    word_map = {}
    for idx, word in enumerate(words):
        if word not in word_map:
            word_map[word] = []
        word_map[word].append(idx + 1)  # индексы 1-based

    pairs = set()

    for i, word in enumerate(words):
        current_idx = i + 1
        reversed_word = word[::-1]
        # случай 1: word + reversed_word дает палиндром
        if reversed_word in word_map:
            for j in word_map[reversed_word]:
                if current_idx != j:
                    if current_idx < j:
                        pairs.add((current_idx, j))
                    else:
                        pairs.add((j, current_idx))
        # случай 2: ищем префиксы word, которые палиндромы, и есть обратный суффикс
        for k in range(1, len(word)):
            prefix = word[:k]
            suffix = word[k:]
            if is_palindrome(prefix):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_map:
                    for j in word_map[reversed_suffix]:
                        if current_idx != j:
                            if j < current_idx:
                                pairs.add((j, current_idx))
                            else:
                                pairs.add((current_idx, j))
        # случай 3: ищем суффиксы word, которые палиндромы, и есть обратный префикс
        for k in range(1, len(word)):
            suffix = word[-k:]
            prefix = word[:-k]
            if is_palindrome(suffix):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_map:
                    for j in word_map[reversed_prefix]:
                        if current_idx != j:
                            if current_idx < j:
                                pairs.add((current_idx, j))
                            else:
                                pairs.add((j, current_idx))
    # преобразуем в отсортированный список
    sorted_pairs = sorted(pairs)
    return sorted_pairs

n = int(input())
words = []
for i in range(n):
    a = input()
    words.append(a)
pairs = find_palindrome_pairs(words)
print(len(pairs))
for a, b in pairs:
    print(a, b)
