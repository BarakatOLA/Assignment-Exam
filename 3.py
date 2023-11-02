def calculate_classes_and_allocation(num_students):
    max_class_size = 30
    min_classes = 2

    # Calculate the minimum number of classes needed
    num_classes = max(min_classes, (num_students + max_class_size - 1) // max_class_size)

    # Calculate the ideal class size and remaining students
    ideal_class_size = num_students // num_classes
    remaining_students = num_students % num_classes

    # Initialize the allocation dictionary
    allocation_dict = {}

    # Distribute the students evenly
    for i in range(num_classes):
        if remaining_students > 0:
            allocation_dict[f'Class {i + 1}'] = ideal_class_size + 1
            remaining_students -= 1
        else:
            allocation_dict[f'Class {i + 1}'] = ideal_class_size

    proposed_classes_str = f'Proposed Allocation: {num_classes} classes'

    return proposed_classes_str, allocation_dict


num_students = int(input("enter your student number:= "))
proposed_allocation_str, allocation = calculate_classes_and_allocation(num_students)
print(proposed_allocation_str)
print(allocation)
