class StudentRecords:
    def __init__(self, student_name, coursework_mark, exam_mark):
        self.student_name = student_name
        self.coursework_mark = coursework_mark
        self.exam_mark = exam_mark
        
def main():
    student_record_list = []
    menu_ui = ( 
        "a. Add new student records",
        "b. Show all student records",
        "c. Delete student records",
        "d. Display overall average coursework mark",
        "e. Display overall average exam mark",
        "f. Display all aggregate marks",
        "g. Display overall average aggregate mark",
        "\nx. Exit\n"        
    )
    
    menu_choice = ''
    while True:
        for i in menu_ui:
            print(i)
        menu_choice = input('Enter option: ')
        
        if menu_choice == 'a':
            input_student_name = input("Student Name: ")
            input_coursework_mark = input("Coursework Mark: ")
            
            while not isinstance(input_coursework_mark, int):
                try:
                    input_coursework_mark = int(input_coursework_mark)
                except ValueError:
                    print("\n[!] Invalid input\n")
                    input_coursework_mark = input("Coursework Mark: ")
                    
            input_exam_mark = input("Exam Mark: ")
            
            while not isinstance(input_exam_mark, int):
                try:
                    input_exam_mark = int(input_exam_mark)
                except ValueError:
                    print("\n[!] Invalid input\n")
                    input_exam_mark = input("Exam Mark: ")
        
            student_records = StudentRecords(
                input_student_name,
                input_coursework_mark,
                input_exam_mark
            )
            
            student_records = tuple((
                student_records.student_name,
                student_records.coursework_mark,
                student_records.exam_mark
                ))
            
            student_record_list.append(student_records)
            
        if menu_choice == 'b':
            for i in student_record_list:
                for ii in i:
                    print(str(ii))
        
if __name__ == "__main__":
    main()