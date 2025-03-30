def setCover(warehouses, stores):

    selected = []
    uncovered_stores = set(stores)

    while uncovered_stores:
        best_warehouse = max(warehouses, key=lambda w: len(w & uncovered_stores))
        selected.append(best_warehouse)

        uncovered_stores -= best_warehouse

    return selected

stores = {1, 2, 3, 4, 5}
warehouses = [
    {1, 2, 3},
    {2, 4},
    {3, 5},
    {4, 5}
]

selected = setCover(warehouses, stores)

print(selected)