import zipfile
import os


def is_zip_file(file):
    x, file_extension = os.path.splitext(file)
    if file_extension.lower() == '.zip':
        return True


def unzip_file(zip_file_path, extract_to_path):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_path)
            print("File {0} extracted successfully".format(zip_file_path.rsplit('\\')[-1]))

    except zipfile.BadZipFile:
        print(f"Error: {zip_file_path} is not a valid ZIP file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_file(file_path):
    try:
        os.remove(file_path)
        print("File {0} deleted successfully \n".format(file_path.rsplit('\\')[-1]))
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except PermissionError:
        print(f"Error: Permission denied to delete {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Replace 'your_zip_file.zip' and 'your_extraction_path' with your actual file and extraction path
    path_to_zip_files = input("Provide the path to zip files: ")
    extract_to_path = input("Provide the path where to be extracted: ")

    # Create the extraction directory if it doesn't exist
    if not os.path.exists(extract_to_path):
        os.makedirs(extract_to_path)

    print("\nAll files getting extracted to {0}...\n".format(extract_to_path))

    zfiles = [path_to_zip_files + '\\' + f for f in os.listdir(path_to_zip_files) if is_zip_file(f) == True]

    for file in zfiles:
        unzip_file(file, extract_to_path)
        delete_file(file)

    print("All files extracred successfully")