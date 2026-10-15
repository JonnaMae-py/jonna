students = []

while True:
    print("\n[1] Add Students")
    print("[2] View Records")
    print("[3] Search Student")
    print("[4] Class Summary")
    print("[5] Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        n = int(input("How many students? "))

        for i in range(n):
            name = input("\nName: ")

            grades = []
            for subject in ["Preliminary","Semifinal","Midterm", "Final"]:
                while True:
                    try:
                        g = float(input(subject + " Grade: "))
                        if 0 <= g <= 100:
                            grades.append(g)
                            break
                        print("Grade must be 0-100.")
                    except:
                        print("Enter a number.")

            avg = sum(grades) / 4

            if avg >= 90:
                status = "Outstanding"
            elif avg >= 85:
                status = "Very Satisfactory"
            elif avg >= 80:
                status = "Satisfactory"
            elif avg >= 75:
                status = "Passed"
            else:
                status = "Failed"

            students.append([name, grades, avg, status])

    elif choice == "2":
        for s in students:
            print(s[0], f"- {s[2]:.2f} -", s[3])

    elif choice == "3":
        name = input("Search name: ")

        for s in students:
            if s[0].lower() == name.lower():
                print("Name:", s[0])
                print("Preliminary:", s[1][0])
                print("Semifinal:", s[1][1])
                print("Midterm:", s[1][2])
                print("Final:", s[1][3])
                print(f"Average: {s[2]:.2f}")
                print("Status:", s[3])
                break
        else:
            print("Student not found.")

    elif choice == "4":
        if students:
            high = max(students, key=lambda x: x[2])
            low = min(students, key=lambda x: x[2])
            passed = sum(s[2] >= 75 for s in students)

            print("Highest:", high[0], f"- {high[2]:.2f}")
            print("Lowest:", low[0], f"- {low[2]:.2f}")
            print(f"Class Average: {sum(s[2] for s in students)/len(students):.2f}")
            print("Passed:", passed)
            print("Failed:", len(students) - passed)
            print(f"Passing Rate: {passed/len(students)*100:.2f}%")
        else:
            print("No records.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
