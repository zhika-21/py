def multiplication_table():
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{i * j:4}", end=" ")  # Format output for alignment
        print()  # Newline after each row

if __name__ == '__main__':
    multiplication_table()