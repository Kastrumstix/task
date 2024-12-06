def all_variants(text):
    n = len(text)
    for i in range(1 << n):
        a = []
        for j in range(n):
            if i & (1 << j):
                a.append(text[j])
        yield ''.join(a)

text = "abc"
for i in all_variants(text):
    print(i)