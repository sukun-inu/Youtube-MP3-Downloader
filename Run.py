import os
import subprocess
import shutil
import time

__version__ = "0.2"

def download_ytdlp():
    # yt-dlp.exeをダウンロードする
    if not os.path.exists('yt-dlp.exe'):
        print('[LOG] yt-dlpをダウンロード中...')
        subprocess.run(['powershell', '-Command', "Start-BitsTransfer -Source 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe' -Destination 'yt-dlp.exe'"], shell=True)

def download_ffmpeg():
    # ffmpeg.exeをダウンロードする
    if not os.path.exists('ffmpeg.exe'):
        print('[LOG] ffmpegをダウンロード中...')
        subprocess.run(['powershell', '-Command', "Start-BitsTransfer -Source 'https://github.com/GyanD/codexffmpeg/releases/latest/download/ffmpeg-6.0-essentials_build.zip' -Destination 'ffmpeg.zip'"], shell=True)
        subprocess.run(['powershell', '-Command', "Expand-Archive -Path 'ffmpeg.zip' -DestinationPath 'ffmpeg'"], shell=True)
        os.rename('ffmpeg\\ffmpeg-6.0-essentials_build\\bin\\ffmpeg.exe', 'ffmpeg.exe')
        os.remove('ffmpeg.zip')
        shutil.rmtree('ffmpeg/ffmpeg-6.0-essentials_build')
        os.rmdir('ffmpeg')

def update_ytdlp():
    # yt-dlpを更新する
    print('[LOG] yt-dlpのアップデートを確認中...')
    subprocess.run(['yt-dlp', '-U'], shell=True)
    if os.path.exists('yt-dlp.exe.old'):
        os.remove('yt-dlp.exe.old')
        subprocess.run(['powershell', '-Command', "Write-Host '[LOG] アップデートに成功しました!' -ForegroundColor Green"], shell=True)
    else:
        subprocess.run(['powershell', '-Command', "Write-Host '[LOG] 最新バージョンを使用中です。' -ForegroundColor Green"], shell=True)

def download_videos():
    # 動画をダウンロードする
    urls = input('YouTubeのURLかプレイリストURLを入力して下さい (コンマで区切って複数入力可能):\n').split(',')
    urls = [url.strip() for url in urls]
    for url in urls:
        cmd = f'yt-dlp --no-check-certificate --extract-audio --audio-format mp3 --audio-quality 192K --add-metadata --newline -o "出力\\%(title)s.%(ext)s" "{url}"'
        subprocess.run(cmd, shell=True)

def main():
    download_ytdlp()
    download_ffmpeg()
    update_ytdlp()
    time.sleep(5)
    while True:
        os.system('cls')
        download_videos()
        print('\n[LOG] ダウンロードと変換が完了しました')
        print('もう一度動画をダウンロードしたい場合Enterを押してください。そのまま終了したい場合はウィンドウを閉じてください。')
        try:
            input()
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()