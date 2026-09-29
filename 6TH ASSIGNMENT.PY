def knapsack_top_down(item_weights, item_values, item_count, bag_capacity, memory):

    if item_count == 0 or bag_capacity == 0:
        return 0

    if memory[item_count][bag_capacity] != -1:
        return memory[item_count][bag_capacity]

    if item_weights[item_count - 1] > bag_capacity:

        memory[item_count][bag_capacity] = knapsack_top_down(
            item_weights,
            item_values,
            item_count - 1,
            bag_capacity,
            memory
        )

    else:

        take_item = item_values[item_count - 1] + knapsack_top_down(
            item_weights,
            item_values,
            item_count - 1,
            bag_capacity - item_weights[item_count - 1],
            memory
        )

        skip_item = knapsack_top_down(
            item_weights,
            item_values,
            item_count - 1,
            bag_capacity,
            memory
        )

        memory[item_count][bag_capacity] = max(take_item, skip_item)

    return memory[item_count][bag_capacity]


item_weights = [2, 1, 3, 2]
item_values = [12, 10, 20, 15]

bag_capacity = 5
item_count = len(item_weights)

memory = [[-1 for index in range(bag_capacity + 1)]
          for index in range(item_count + 1)]

best_value = knapsack_top_down(
    item_weights,
    item_values,
    item_count,
    bag_capacity,
    memory
)

print("Maximum value using Top-Down:", best_value)