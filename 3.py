def main():
    N, M, Q = map(int, input().split())
    columns = input().split()
    table = [list(map(int, input().split())) for _ in range(N)]

    # Словарь для индексации столбцов по их названиям
    column_indexes = {name: index for index, name in enumerate(columns)}


    for _ in range(Q):
        column_name, condition, value = input().split()
        column_index = column_indexes[column_name]
        value = int(value)

        table = [row for row in table if (condition == '>' and row[column_index] > value) or
                 (condition == '<' and row[column_index] < value)]

    total_sum = sum(sum(row) for row in table)
    print(total_sum)


if __name__ == '__main__':
    main()
