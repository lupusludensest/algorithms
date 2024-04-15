def duplicate_count(text):
    seen = set()
    dups = set()

    text = text.upper()

    for i in text:
        if i in seen:
            dups.add(i)
        else:
            seen.add(i)

    return len(dups)

print(duplicate_count("Indivisibilities"))