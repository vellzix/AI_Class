def search_element(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return 0

x = [5, 5, 10, 3, 2, 6, 7]
y1 = 4
y2 = 7

index_y1 = search_element(x, y1)
index_y2 = search_element(x, y2)

print("y1:", index_y1)
print("y2:", index_y2)
