subject_names = {
    0: 'maths',
    1: 'physics',
    2: 'chemistry',
    3: 'biology',
    4: 'english',
    5: 'history',
    6: 'geography',
    7: 'computer science',
}

class_types = {
    0: 'lecture',
    1: 'practice',
}


class SubjectClass:
    def __init__(self, subject_name, class_type):
        self.subject_name = subject_name
        self.class_type = class_type

    def __str__(self):
        return f'{self.subject_name} {self.class_type}'
