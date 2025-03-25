path = "/mnt/1_1"
dir1 = ["dir1", "dir2", "dir3", "dir4"]

cmd = f"rm -rf  {' '.join([f'{path}/{d}' for d in dir1])}"
print(cmd)