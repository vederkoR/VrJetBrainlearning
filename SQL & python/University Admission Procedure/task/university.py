import os

max_num_students = int(input())
deps = biotech, chemistry, engineering, mathematics, physics = ["biotech", (2, 3)], \
                                                               ["chemistry", (3,)], \
                                                               ["engineering", (4, 5)], \
                                                               ["mathematics", (4,)], \
                                                               ["physics", (2, 4)]


def del_files_for_test():
    for dep in deps:
        if os.path.exists(dep[0] + ".txt"):
            os.remove(dep[0] + ".txt")


def main():
    del_files_for_test()
    with open('applicants.txt', mode='r') as file:
        all_students = [student.strip().split(" ") for student in file.readlines()]

        bio_students_rnd_1 = sorted([i for i in all_students if i[6] == "Biotech"],
                                    key=lambda x: (-int(x[2]) - int(x[3]), x[0] + x[1]))
        bio_students_rnd_2 = sorted([i for i in all_students if i[7] == "Biotech"],
                                    key=lambda x: (-int(x[2]) - int(x[3]), x[0] + x[1]))
        bio_students_rnd_3 = sorted([i for i in all_students if i[8] == "Biotech"],
                                    key=lambda x: (-int(x[2]) - int(x[3]), x[0] + x[1]))

        che_students_rnd_1 = sorted([i for i in all_students if i[6] == "Chemistry"],
                                    key=lambda x: (-int(x[3]), x[0] + x[1]))
        che_students_rnd_2 = sorted([i for i in all_students if i[7] == "Chemistry"],
                                    key=lambda x: (-int(x[3]), x[0] + x[1]))
        che_students_rnd_3 = sorted([i for i in all_students if i[8] == "Chemistry"],
                                    key=lambda x: (-int(x[3]), x[0] + x[1]))

        eng_students_rnd_1 = sorted([i for i in all_students if i[6] == "Engineering"],
                                    key=lambda x: (-int(x[4]) - int(x[5]), x[0] + x[1]))
        eng_students_rnd_2 = sorted([i for i in all_students if i[7] == "Engineering"],
                                    key=lambda x: (-int(x[4]) - int(x[5]), x[0] + x[1]))
        eng_students_rnd_3 = sorted([i for i in all_students if i[8] == "Engineering"],
                                    key=lambda x: (-int(x[4]) - int(x[5]), x[0] + x[1]))

        math_students_rnd_1 = sorted([i for i in all_students if i[6] == "Mathematics"],
                                     key=lambda x: (-int(x[4]), x[0] + x[1]))
        math_students_rnd_2 = sorted([i for i in all_students if i[7] == "Mathematics"],
                                     key=lambda x: (-int(x[4]), x[0] + x[1]))
        math_students_rnd_3 = sorted([i for i in all_students if i[8] == "Mathematics"],
                                     key=lambda x: (-int(x[4]), x[0] + x[1]))

        phis_students_rnd_1 = sorted([i for i in all_students if i[6] == "Physics"],
                                     key=lambda x: (-int(x[4]) - int(x[2]), x[0] + x[1]))
        phis_students_rnd_2 = sorted([i for i in all_students if i[7] == "Physics"],
                                     key=lambda x: (-int(x[4]) - int(x[2]), x[0] + x[1]))
        phis_students_rnd_3 = sorted([i for i in all_students if i[8] == "Physics"],
                                     key=lambda x: (-int(x[4]) - int(x[2]), x[0] + x[1]))

    students_dist = [bio_students_rnd_1, che_students_rnd_1, eng_students_rnd_1,
                     math_students_rnd_1, phis_students_rnd_1,
                     bio_students_rnd_2, che_students_rnd_2, eng_students_rnd_2,
                     math_students_rnd_2, phis_students_rnd_2,
                     bio_students_rnd_3, che_students_rnd_3, eng_students_rnd_3,
                     math_students_rnd_3, phis_students_rnd_3]
    print(len(students_dist))
    accepted_students = []
    for inx, eval_round in enumerate(students_dist):
        department = deps[inx % 5]
        for student in eval_round:
            if len(department) == max_num_students + 2:
                break
            if student in accepted_students:
                continue
            department.append(student)
            accepted_students.append(student)

    for dep in deps:
        term = dep[2:]
        for student in sorted(term, key=lambda x: (-sum([int(x[i]) for i in dep[1]]), x[0] + x[1])):
            with open(dep[0] + '.txt', mode='a+') as file:
                file.write(f"{student[0]} {student[1]} {sum([float(student[i]) for i in dep[1]]) / len(dep[1])}\n")


if __name__ == '__main__':
    main()
