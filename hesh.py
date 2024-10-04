

book = {}
book["orange"] = 0.67
book["milk"] = 1.49
book["avokado"] = 1.49

print(book)
print(book.get("avokado"))
print(book.get("avokado1"))

for i in book:
    print(i, end=' ')


