import os
import random
import subprocess

# The folder containing your video files
FOLDER_PATH = 'C:/Users/ftama/Documents/Wallpapers'


def get_video_files(folder_path):
    """Returns a list of video files in the given folder, excluding the current wallpaper."""
    video_extensions = (
        '.mp4', '.avi', '.mov')  # Add or remove extensions as needed
    files = os.listdir(folder_path)
    return [f for f in files if f.endswith(video_extensions) and f not in ('wallpaper', 'wallpaper.mp4')]


def rename_random_video(folder_path):
    """Renames a random video file to 'wallpaper' and the previous 'wallpaper' to a random name."""
    videos = get_video_files(folder_path)
    if not videos:
        print("No video files found.")
        return

    current_wallpaper_path = os.path.join(folder_path, 'wallpaper.mp4')
    if os.path.exists(current_wallpaper_path):
        original_name = 'renamed_' + \
            ''.join(random.choices(
                'abcdefghijklmnopqrstuvwxyz1234567890', k=5)) + '.mp4'
        os.rename(current_wallpaper_path, os.path.join(
            folder_path, original_name))

    new_wallpaper = random.choice(videos)
    new_wallpaper_path = os.path.join(folder_path, new_wallpaper)
    os.rename(new_wallpaper_path, current_wallpaper_path)


def restart_lively_wallpaper():
    """Attempts to stop and then restart the Lively Wallpaper application using PowerShell."""
    try:
        # Stop any existing instance of Lively Wallpaper
        lively_app_id = "12030rocksdanister.LivelyWallpaper_97hta09mmv6hy!App"
        subprocess.call(["taskkill", "/F", "/IM", "Lively.exe"])

        # Restart Lively Wallpaper using PowerShell command
        subprocess.call(["powershell", "Start-Process", f"explorer shell:appsfolder\\{lively_app_id}"])
    except Exception as e:
        print(f"Failed to restart Lively Wallpaper: {e}")

def main():
    rename_random_video(FOLDER_PATH)
    restart_lively_wallpaper()


if __name__ == "__main__":
    main()
