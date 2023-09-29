import os
import shutil


def file_sort(start_directory, result_directory: str, video_extensions = [".mp4"], music_ext = [".mp3"], text_ext = [".txt"]):
    if os.path.exists(start_directory):
        for item in os.listdir(start_directory):
            item_path = os.path.join(start_directory, item)
            for ext in video_extensions:
                if item.endswith(ext):
                    texts_dir = os.path.join(result_directory, "texts")
                    if not os.path.exists(texts_dir):
                        os.mkdir(texts_dir)
                    shutil.move(item_path, os.path.join(texts_dir, item))
            for ext in music_ext:
                if item.endswith(ext):
                    music_dir = os.path.join(result_directory, "music")
                    if not os.path.exists(music_dir):
                        os.mkdir(music_dir)
                        shutil.move(item_path, os.path.join(music_dir, item))
            for ext in text_ext:
                if item.endswith(ext):
                    videos_dir = os.path.join(result_directory, "videos")
                    if not os.path.exists(videos_dir):
                        os.mkdir(videos_dir)
                        shutil.move(item_path, os.path.join(videos_dir, item))

    else:
        print("Исходная папка не найдена.")


source = r"C:\Users\Александр\Desktop\Geek Brains\Python курс 2 практика\S7\start_dir"
destination = r"C:\Users\Александр\Desktop\Geek Brains\Python курс 2 практика\S7\result_dir"
videos = [".mp4", ".avi"]
music = [".mp3", ".wav"]
texts = [".txt", ".docx"]
file_sort(source, destination, video_extensions=videos, music_ext=music, text_ext=texts)
