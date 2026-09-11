from pathlib import Path
import shutil


def get_category(extension):
    extension = extension.lower()

    if extension in [".jpg", ".jpeg", ".png"]:
        return "Images"

    elif extension in [".pdf", ".txt"]:
        return "Documents"

    elif extension in [".mp3", ".wav"]:
        return "Audio"

    elif extension == ".py":
        return "Python"

    elif extension in [".zip", ".rar"]:
        return "Archives"
    elif extension == ".exe":
        return "Apps"
    elif extension in ".iso":
        return "ISO_Images"

    else:
        return "Other"


def scan_folder(folder_path):
    if not folder_path.exists() or not folder_path.is_dir():
        print("Folder not available!")
        return

    files_found = 0

    print("\n================================")
    print("PREVIEW")
    print("================================")

    for item in folder_path.iterdir():

        if item.is_file():
            files_found += 1

            extension = item.suffix.lower()
            category = get_category(extension)

            print(f"{item.name} -> {category}/")

    if files_found == 0:
        print("No files were found to organize.")

    print("================================\n")


def get_unique_destination(destination):
    if not destination.exists():
        return destination

    parent = destination.parent
    stem = destination.stem
    suffix = destination.suffix

    counter = 1

    while True:
        new_name = f"{stem}_{counter}{suffix}"
        new_destination = parent / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_folder(folder_path):
    if not folder_path.exists() or not folder_path.is_dir():
        print("Folder not available!")
        return

    files_moved = 0
    summary = {}

    for item in list(folder_path.iterdir()):

        if not item.is_file():
            continue

        extension = item.suffix.lower()

        category = get_category(extension)

        destination_folder = folder_path / category

        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / item.name

        destination = get_unique_destination(destination)

        print(f"Moving {item.name} -> {category}/{destination.name}")

        shutil.move(str(item), str(destination))

        files_moved += 1

        if category in summary:
            summary[category] += 1
        else:
            summary[category] = 1

    print("\n================================")
    print("ORGANIZATION COMPLETE")
    print("================================")

    if files_moved == 0:
        print("No files were found to organize.")
        return

    print(f"Files moved: {files_moved}")

    print("\nFiles by category:")

    for category, count in summary.items():
        print(f"{category}: {count}")

    print("================================\n")
