def calculate_classes_and_allocation(num_students):
    if num_students <= 0:
        print("Please enter a valid number of students.")
        return

    # Define the maximum number of students per class (you can adjust this as needed)
    max_students_per_class = 30

    # Calculate the number of classes needed
    num_classes = (num_students + max_students_per_class - 1) // max_students_per_class

    # Initialize the allocation dictionary
    allocation = {}

    # Allocate students to classes
    for class_num in range(1, num_classes + 1):
        students_in_class = min(max_students_per_class, num_students)
        allocation[f"Class {class_num}"] = students_in_class
        num_students -= students_in_class

    # Print the proposed number of classes and the allocation
    print(f"Proposed Number of Classes: {num_classes}")
    print("Class Allocation:")
    for class_name, students in allocation.items():
        print(f"{class_name}: {students} students")

# Example usage:
num_students = 31
calculate_classes_and_allocation(num_students)