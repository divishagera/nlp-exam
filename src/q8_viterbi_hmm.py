# 8: Viterbi Algorithm Using HMM for POS Tagging

import nltk

tags = ["DT", "NN", "VB"]

start_p = {
    "DT": 0.6,
    "NN": 0.2,
    "VB": 0.2
}

trans_p = {
    "DT": {"DT": 0.05, "NN": 0.90, "VB": 0.05},
    "NN": {"DT": 0.1, "NN": 0.3, "VB": 0.6},
    "VB": {"DT": 0.4, "NN": 0.4, "VB": 0.2}
}

emit_p = {
    "DT": {"the": 0.50, "a": 0.50, "dog": 0.0, "cat": 0.0, "barks": 0.0},
    "NN": {"dog": 0.4, "cat": 0.4, "bark": 0.1, "barks": 0.1},
    "VB": {"run": 0.4, "barks": 0.4, "dog": 0.1, "cat": 0.1}
}

words = input("Enter a sentence: ").lower().split()
n = len(words)
eps = 1e-6

v = [{} for _ in range(n)]
back = [{} for _ in range(n)]

for s in tags:
    v[0][s] = start_p[s] * emit_p[s].get(words[0], eps)
    back[0][s] = None

for t in range(1, n):
    for s in tags:
        prev = max(tags, key=lambda p: v[t - 1][p] * trans_p[p][s])
        v[t][s] = v[t - 1][prev] * trans_p[prev][s] * emit_p[s].get(words[t], eps)
        back[t][s] = prev

best = max(tags, key=lambda s: v[n - 1][s])
path = [best]

for t in range(n - 1, 0, -1):
    path.insert(0, back[t][path[0]])

for w, tag in zip(words, path):
    print(w, "->", tag)
