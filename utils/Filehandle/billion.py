import os
import random
import string
import shutil
import time

ROOT_DIR = "C:\\New"  # Change the root directory path as per your requirement
DEPTH = 5
WIDTH = 10
NUM_FILES_PER_DIRECTORY = 10 ** 5
MIN_FILE_SIZE = 4 * 1024  # 4 KB
MAX_FILE_SIZE = 4 * 1024 * 1024  # 1 MB


class FilesystemLoader:
    """
    FilesystemLoader is a class that facilitates the creation
    of a filesystem with a specified structure and number of files.
    """

    def __init__(self, root_dir, depth, width, num_files_per_directory):
        """
        Initialize the FilesystemLoader object.

        :param root_dir: The root directory where the filesystem will
        be created.
        :param depth: The number of directory levels in the filesystem.
        :param width: The number of subdirectories in each directory.
        :param num_files_per_directory: The number of files in each
        directory.
        """
        self.root_dir = root_dir
        self.depth = depth
        self.width = width
        self.num_files_per_directory = num_files_per_directory

        if os.path.exists(self.root_dir):
            shutil.rmtree(self.root_dir)

    def create_directory_structure(self, path, level):
        """
        Recursively create the directory structure.

        :param path: The current path where the directory will be created.
        :param level: The current level of the directory.
        """
        if level == 0:
            return

        for i in range(self.width):
            subdir = os.path.join(path, f"dir{i}_{self.depth+1}")
            if not os.path.exists(subdir):
                os.makedirs(subdir)
            self.create_directory_structure(subdir, level-1)
            self.create_files(subdir)

    def create_files(self, directory):
        """
        Create the specified number of files in the given directory.

        :param directory: The directory where the files will be created.
        """
        for i in range(self.num_files_per_directory):
            file_path = os.path.join(directory, f"file{i+1}.txt")
            file_size = random.randint(MIN_FILE_SIZE, MAX_FILE_SIZE)

            with open(file_path, "w") as file:
                random_text = ''.join(random.choice(string.ascii_letters +
                                      string.digits) for _ in range(file_size))
                file.write(random_text)

    def load_filesystem(self):
        """
        Load the filesystem by creating the directory structure and files.
        """
        start_time = time.time()
        os.makedirs(self.root_dir, exist_ok=True)
        self.create_directory_structure(self.root_dir, self.depth)
        end_time = time.time()
        total_time = end_time - start_time
        print("Filesystem loaded successfully in {:.2f} seconds.".
              format(total_time))

if __name__ == "__main__":
    filesystem_loader = FilesystemLoader(ROOT_DIR, DEPTH, WIDTH,
                                         NUM_FILES_PER_DIRECTORY)
    filesystem_loader.load_filesystem()
