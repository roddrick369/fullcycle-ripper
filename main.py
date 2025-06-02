from platforms.login import login
from platforms.api import get_courses, get_learning_paths, get_classrooms, get_modules
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
                    #print(learning_paths["learning_paths"])
                    break
                else:
                    print(f"Please enter a number between 1 and {counter}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

    if course_id == 215: # type: ignore
        for catalog in learning_paths["learning_paths"]: # type: ignore
            catalog_id = catalog["id"]
            classrooms = get_classrooms(catalog_id, classroom_id) # type: ignore

            for chapter in classrooms["courses"]:
                chapter_id = chapter["id"]
                modules = get_modules(chapter_id, classroom_id) # type: ignore

                print(modules["content"])
    else:
        for catalog in learning_paths["learning_paths"]: # type: ignore
            catalog_id = catalog["id"]
            print(f"id: {catalog_id}, nome: {catalog["nome"]}")

            if catalog["total_conteudo"] > 0:
                modules = get_modules(catalog_id, classroom_id) # type: ignore
                print(modules["content"][:40]) # type: ignore
            
    
if __name__ == "__main__":
    main()
