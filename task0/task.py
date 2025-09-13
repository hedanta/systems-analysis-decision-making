import csv
import sys

def get_matrix(rows, directed=False):
    edges = []
    v = set()
    for row in rows:
        a_str, b_str = row.strip().split(',')
        a, b = int(a_str), int(b_str)
        edges.append((a, b))
        v.add(a)
        v.add(b)

    n = max(v)
    matrix = [[0] * n for _ in range(n)]

    for a, b in edges:
        matrix[a-1][b-1] = 1
        if not directed:
            matrix[b-1][a-1] = 1

    return matrix



def main():
    if len(sys.argv) < 2:
        print('usage: python task.py task.csv')
        return
    
    with open(sys.argv[1], newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    str_rows = [','.join(row) for row in rows]
    matrix = get_matrix(str_rows)

    for row in matrix:
        print(row)


if __name__ == '__main__':
    main()