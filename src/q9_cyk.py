# 9: Cocke-Younger-Kasami (CYK) Algorithm

def cyk_parse(words, grammar):
    n = len(words)
    if n == 0:
        return False

    table = [[set() for _ in range(n - span)] for span in range(n)]

    for i, word in enumerate(words):
        for lhs, rhs_list in grammar.items():
            if (word,) in rhs_list:
                table[0][i].add(lhs)

    for span in range(1, n):
        for i in range(n - span):
            for split in range(span):
                left = table[split][i]
                right = table[span - 1 - split][i + 1 + split]
                for lhs, rhs_list in grammar.items():
                    for rhs in rhs_list:
                        if len(rhs) == 2 and rhs[0] in left and rhs[1] in right:
                            table[span][i].add(lhs)

    return "S" in table[n - 1][0]

cnf_grammar = {
    "S": [("NP", "VP")],
    "VP": [("V", "NP"), ("eats",)],
    "NP": [("she",), ("apples",)],
    "V": [("eats",)],
}

user_input = input("Enter space-separated words to test (default 'she eats apples'): ").strip()
tokens = user_input.lower().split() if user_input else ["she", "eats", "apples"]
print("Tokens:", tokens)
print("Belongs to grammar language:", cyk_parse(tokens, cnf_grammar))
