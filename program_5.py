# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def get_courses():
    """Prompt the user to enter course ID/name pairs until they type 'done'."""
    courses = {}

    print("Enter course ID and name pairs.")
    print("Example — Course ID: COS 2005  |  Course Name: Python Programming")
    print("Type 'done' as the course ID when you are finished.\n")

    while True:
        course_id = input("Course ID (or 'done' to stop): ").strip()

        if course_id.lower() == "done":
            break

        # Validate that the course ID contains a space (e.g. "COS 2005")
        if " " not in course_id:
            print("  Please enter a valid course ID with a subject and number (e.g. 'COS 2005').\n")
            continue

        course_name = input("Course Name: ").strip()
        courses[course_id.upper()] = course_name
        print(f"  '{course_id.upper()}' added.\n")

    return courses


def search_courses(courses, subject):
    """Return all courses whose ID starts with the given subject prefix."""
    subject = subject.strip().upper()
    return {cid: name for cid, name in courses.items() if cid.startswith(subject)}


def display_results(matches, subject):
    """Print the matching courses, or a not-found message."""
    print(f"\nCourses with subject '{subject}':")
    print("-" * 35)

    if matches:
        for course_id, course_name in sorted(matches.items()):
            print(f"  {course_id:<12} {course_name}")
    else:
        print(f"  No courses found for subject '{subject}'.")


if __name__ == "__main__":
    courses = get_courses()

    if not courses:
        print("No courses were entered.")
    else:
        subject = input("\nEnter a subject to search for (e.g., 'COS'): ")
        matches = search_courses(courses, subject)
        display_results(matches, subject.strip().upper())
