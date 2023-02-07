def format_text(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [" : ".join(line.strip().split()) + "\n" for line in lines]

    with open(filename, 'w') as file:
        file.writelines(lines)

# Reverts the grades.txt file back to its original, unformatted state.abs(x)
def revert_format_text(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.replace(" : ", " ") for line in lines]

    with open(filename, 'w') as file:
        file.writelines(lines)

def text_to_dict(filename, dict):
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split(" : ")
            for i in range(0, len(values), 2):
                student = values[i]
                grade = float(values[i+1])
                dict[student] = grade

def average_marks(dict):
    values = list(map(float, dict.values()))
    mean = sum(values) / len(values)
    
    return mean

def main():
    data = {}

    format_text("grades.txt")
    text_to_dict("grades.txt", data)

    for key, value in data.items():
        print(key, value)

    print("AVERAGE:", average_marks(data))
    revert_format_text("grades.txt")

if __name__ == "__main__":
    main()
