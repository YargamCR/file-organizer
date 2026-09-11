from pathlib import Path
import organizer
import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def get_folder():
    folder_input = input(
        "Enter the folder path you want to organize: ").strip()

    folder_path = Path(folder_input).expanduser()

    if not folder_path.exists():
        print("\nThe selected folder does not exist.")
        return None

    if not folder_path.is_dir():
        print("\nThe selected path is not a folder.")
        return None

    return folder_path


def show_menu():
    print("================================")
    print("        FILE ORGANIZER")
    print("================================")
    print("1. Preview organization")
    print("2. Organize folder")
    print("3. Change folder")
    print("4. Exit")
    print("================================")


clear_terminal()

folder_path = get_folder()

while True:

    if folder_path is None:
        print("\nPlease select a valid folder.")
        folder_path = get_folder()
        continue

    print(f"\nCurrent folder: {folder_path}\n")

    show_menu()

    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("\nPlease enter a valid number.")
        input("\nPress Enter to continue...")
        clear_terminal()
        continue

    match option:

        case 1:
            clear_terminal()

            organizer.scan_folder(folder_path)

            input("Press Enter to continue...")
            clear_terminal()

        case 2:
            clear_terminal()

            print("You are about to organize:")
            print(f"\n{folder_path}\n")
            print("Files will be moved into category folders.")

            confirmation = input(
                "\nContinue? yes/no: "
            ).strip().lower()

            if confirmation == "yes":
                print()
                organizer.organize_folder(folder_path)
            else:
                print("\nOperation cancelled.")

            input("\nPress Enter to continue...")
            clear_terminal()

        case 3:
            clear_terminal()

            folder_path = get_folder()

            clear_terminal()

        case 4:
            clear_terminal()
            print("Thank you for using File Organizer!")
            break

        case _:
            print("\nPlease choose an option between 1 and 4.")
            input("\nPress Enter to continue...")
            clear_terminal()
