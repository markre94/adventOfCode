data = "1321131112"

# Perform 40 iterations
for _ in range(50):
    res = []  # Reset results for each iteration
    i = 0
    while i < len(data):
        num = data[i]
        num_count = 1

        # Count consecutive digits
        while i + 1 < len(data) and data[i] == data[i + 1]:
            num_count += 1
            i += 1

        # Append count and number to the result
        res.append(f"{num_count}{num}")
        i += 1

    # Prepare the next input
    data = "".join(res)

# Final result
print(len(data))
