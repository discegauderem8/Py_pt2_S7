import os
import shutil


def rename_files(directory, target_name, num_digits, start_extension, target_extension, name_range=None):
    counter = 1
    done_count = 0
    for filename in os.listdir(directory):
        if filename.endswith(start_extension):
            name_part = filename[name_range[0] - 1:name_range[1]]
            new_filename = f"{name_part}_{target_name}{counter:0{num_digits}}{target_extension}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            counter += 1
            done_count += 1

    if done_count > 0:
        print("Файлы успешно переименованы.")
    else:
        print("Файлов с указанным разрешением не найдено.")
