

def binary_to_decimal(chromosome_value, lower_bound, upper_bound, precision):
    result = []
    for i in range(0, len(chromosome_value), precision):
        binary = chromosome_value[i:i+precision]
        decimal = int("".join(map(str, binary)), 2)
        max_decimal = 2**len(binary) - 1
        result.append(lower_bound + (upper_bound - lower_bound) * (decimal / max_decimal))
    return result

