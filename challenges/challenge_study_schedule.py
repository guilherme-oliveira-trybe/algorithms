def study_schedule(permanence_period, target_time):
    students_quantity = 0

    for entry, exit in permanence_period:
        if entry is None or exit is None or target_time is None:
            return None

        if type(entry) is str or type(exit) is str:
            return None

        if int(entry) <= target_time <= int(exit):
            students_quantity += 1

    return students_quantity
