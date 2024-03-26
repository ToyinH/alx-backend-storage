#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score
"""
def top_students(mongo_collection):
    """
    Python function that returns all students sorted by average score
    """
    students = mongo_collection.find({}, {"name": 1, "topics": 1})  # Fetch all students
    student_list = list(students)  # Convert cursor to list

    # Calculate average score for each student
    for student in student_list:
        scores = [topic['score'] for topic in student['topics']]
        average_score = sum(scores) / len(scores)
        student['averageScore'] = average_score

    # Sort students by average score in descending order
    sorted_students = sorted(student_list, key=lambda x: x['averageScore'], reverse=True)
    
    return sorted_students
