def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def sort_words(words):
    sorted_words = sorted(words)
    return sorted_words

def reverse_lines(lines):
    reversed_lines = [line.strip()[::-1] for line in lines]
    print('\n'.join(reversed_lines))

def last_n_lines(lines, n):
    last_n = lines[-n:]
    for line in last_n:
        print(line)

def main():
    while True:
        file_path = input("Enter a file path: ")
        task = input("Enter a task: ")

        lines = read_file(file_path)

        if task == "sort":
            words = ' '.join(lines).split()
            result = sort_words(words)
            print(result)
        elif task == "rev":
            reversed_lines = reverse_lines(lines)
            for line in reversed_lines:
                print(line)
        elif task == "last":
            n = int(input("Enter a number: "))
            last_n = last_n_lines(lines, n)
            for line in last_n:
                print(line.strip())

        again = input("Do you want to continue? (yes/no): ")
        if again.lower() != "yes":
            break

if __name__ == "__main__":
    main()