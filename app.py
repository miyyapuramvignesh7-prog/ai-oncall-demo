def calculate_average(total: float, count: int) -> float:
    # Intentional bug: crashes with ZeroDivisionError if count is 0
    return total / count
