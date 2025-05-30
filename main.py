from platforms.login import login
from platforms.api import get_courses, get_learning_paths
from clear_screen import clear

def main():
    username = input("Enter your email: ")
    password = input("Enter your password: ")

    try:
        token = login(username, password)

        courses = get_courses()
        clear()
        print("Courses retrieved successfully:")


        counter = 0
        for course in courses:
            counter += 1
            print(f'{counter}. {course["category"]["name"]}')

        while True:
            if counter == 0:
                print("No courses found.")
                break

            try:
                course_index = int(input("Enter the course number to download it: "))
                if 1 <= course_index <= counter:
                    clear()
                    course_index -= 1  # type: ignore  Adjust for zero-based index
                    course_id = courses[course_index]['category']['id']
                    classroom_id = courses[course_index]['classroom']['id']
                    learning_paths = get_learning_paths(course_id, classroom_id)
                    if course_id != 215:
                        learning_paths = {"learning_paths": learning_paths}
                    print(learning_paths["learning_paths"])
                    break
                else:
                    print(f"Please enter a number between 1 and {counter}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
