import matplotlib.pyplot as plt

def merge_sort(values):
    if len(values) <= 1:
        return

    # Split the list into two halves
    middle = len(values) // 2
    l = values[:middle]
    r = values[middle:]

    # Recursively sort both halves
    merge_sort(l)
    merge_sort(r)

    # Merge the sorted halves
    merge(values, l, r)


def merge(values, l, r):
    l_index = 0
    r_index = 0
    target_index = 0

    # Compare elements from both halves and place the smaller one first
    while l_index < len(l) and r_index < len(r):
        if l[l_index] <= r[r_index]:
            values[target_index] = l[l_index]
            l_index += 1
        else:
            values[target_index] = r[r_index]
            r_index += 1
        target_index += 1

    # Copy remaining elements from the left and right halves
    while l_index < len(l):
        values[target_index] = l[l_index]
        l_index += 1
        target_index += 1

    while r_index < len(r):
        values[target_index] = r[r_index]
        r_index += 1
        target_index += 1


def plot_values(values, title):
    positions = range(len(values))
    plt.plot(positions, values, marker="o")
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()


def main():
    values = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    plot_values(values, "Before sorting")
    merge_sort(values)
    plot_values(values, "After sorting")


if __name__ == "__main__":
    main()