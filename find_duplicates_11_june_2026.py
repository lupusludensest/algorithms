def find_duplicates(user_ids: list) -> dict:
    count_map = {}
    for uid in user_ids:
        count_map[uid] = count_map.get(uid, 0) + 1
    return {uid: count for uid, count in count_map.items() if count > 1}

if __name__ == "__main__":
    user_ids = [1, 2, 3, 2, 4, 5, 1, 6, 3, 3, 123, 234, 123, 234, 234, 234]
    duplicates = find_duplicates(user_ids)
    print("Duplicates:", duplicates)
