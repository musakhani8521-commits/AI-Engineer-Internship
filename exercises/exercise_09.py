def calculate_average(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30]))