a = [3, 2, 1, 4, 6, 7, 1]


num_of_swaps = 0
for i in a:
    for j in range(len(a)-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            num_of_swaps = num_of_swaps + 1
    if num_of_swaps == 0: break
print(f"Array is sorted in {num_of_swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")