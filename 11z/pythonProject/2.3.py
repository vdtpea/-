sequence = [int(input(f"Введите {i+1}-й элемент последовательности: ")) for i in range(16)]
even_index_values = [sequence[i] for i in range(1, len(sequence), 2)]

print("Исходная последовательность:", sequence)
print("Список из значений под четными номерами:", even_index_values)
