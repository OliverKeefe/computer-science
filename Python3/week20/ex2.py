"""
Exercise 2
1. Create a new text file identical to the following (you can copy the text from page 2 of this
document). The text file contains the names and current marks for a class of students. You
will note that each student record is on a new line in the text file, and the numbers following
each student name represent the marks currently obtained by each student for completed
assignments.

2. Write a simple program to first prompt the user to enter the filename of the text file that they
wish to open. The program should then open the text file, read the contents of the file, and
store this in a suitable Python data structure. Make sure you include a suitable exception
handling (try ... except) structure that will inform the user if there is a problem loading
the file and allows the user to enter an alternative filename if there is a problem.

3. Once the data is successfully loaded, print out the data in a neatly formatted manner (see an
example output below).

4. Calculate the average mark for each student and print these out with the data in task 3. Then
also calculate the average mark for the class and print this out at the end.

"""
def main():
    class_total = 0
    class_count = 0

    while True:
        file_path = input("Enter a filename: ")   

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    data = line.split()
                    name = " ".join(data[:-2])
                    marks = []
                    if len(data) > 2:
                        marks = [float(x) for x in data[-2:]]
                    avg = sum(marks) / len(marks) if marks else 0.0
                    print(f"{name}:")
                    print(f"Marks: {', '.join(str(m) for m in marks)}, Average: {avg:.2f}")
                    class_total += sum(marks)
                    class_count += len(marks)
                class_avg = class_total / class_count if class_count else 0.0
                print(f"Total Average: {class_avg:.2f}")

        except FileNotFoundError:
            print("[!] Error, invalid file path.")

if __name__ == "__main__":
    main()


    