max_num_students = int(input())
deps = biotech, chemistry, engineering, mathematics, physics = ["Biotech"], ["Chemistry"], ["Engineering"], \
                                                               ["Mathematics"], ["Physics"]


def distribution(student, i):
    match student[i]:
        case "Mathematics":
            if len(mathematics) > max_num_students:
                return False
            mathematics.append(student)
        case "Physics":
            if len(physics) > max_num_students:
                return False
            physics.append(student)
        case "Biotech":
            if len(biotech) > max_num_students:
                return False
            biotech.append(student)
        case "Chemistry":
            if len(chemistry) > max_num_students:
                return False
            chemistry.append(student)
        case "Engineering":
            if len(engineering) > max_num_students:
                return False
            engineering.append(student)
    return True


def main():
    with open('applicants.txt', mode='r') as file:
        all_students = sorted([student.strip().split(" ") for student in file.readlines()],
                              key=lambda x: (-float(x[2]), x[0] + x[1]))
    accepted_student = []
    for i in range(3, 6):
        for student in all_students:
            result = distribution(student, i)
            if result:
                accepted_student.append(student)
            if all([len(dep) == max_num_students for dep in deps]):
                break
        all_students = [i for i in all_students if i not in accepted_student]
        accepted_student = []

    for dep in deps:
        print(dep[0])
        term = dep[1:]
        for student in sorted(term, key=lambda x: -float(x[2])):
            print(student[0], student[1], student[2])
        print()


if __name__ == '__main__':
    main()