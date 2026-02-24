import time
import shutil
from pathlib import *
from easyfile import *



picture = ['png', 'jpg', 'jpeg', 'bmp', 'webp', 'gif']
musics = ['mp3', 'wav', 'ogg']
video = ['mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv', 'webm']
documents = ['pdf', 'docx', 'doc', 'pptx', 'ppt', 'xlsx', 'xls', 'hwp', 'hwpx']
data = ['json', 'xml', 'yaml', 'yml', 'csv', 'db', 'sql']
text = ['txt', 'log', 'md']
code = ['py', 'c', 'cpp', 'cc', 'cs', 'java', 'lua', 'rb', 'go', 'rs', 'swift', 'kt', 'dart', 'sh', 'bat', 'ps1', 'h',
        'hpp']
web = ['html', 'htm', 'css', 'js', 'ts', 'jsx', 'tsx']
archive = ['zip', 'rar', '7z', 'tar', 'gz']

def watch(paths):
    items = [os.path.join(paths, i) for i in os.listdir(paths)]
    for i in items:
        if os.path.isfile(i):
            try:
                ext = Path(i).name.lower().split('.')[-1]
                if ext in picture:
                    os.makedirs(f'{paths}/사진', exist_ok=True)
                    shutil.move(i, os.path.join(f'{paths}/사진', os.path.basename(Path(i).name)))
                elif ext in code:
                    os.makedirs(f'{paths}/코드', exist_ok=True)
                    shutil.move(i, os.path.join(f'{paths}/코드', os.path.basename(Path(i).name)))
                elif ext in musics:
                    os.makedirs(f'{paths}/음악과 음향', exist_ok=True)
                    shutil.move(i, os.path.join(f'{paths}/음악과 음향', os.path.basename(Path(i).name)))
                elif ext in video:
                    os.makedirs(f'{paths}/동영상', exist_ok=True)
                    shutil.move(i, os.path.join(f'{paths}/동영상', os.path.basename(Path(i).name)))
                elif ext in documents:
                    os.makedirs(f'{paths}/각종 문서', exist_ok=True)
                    shutil.move(i, os.path.join(f'{paths}/각종 문서', os.path.basename(Path(i).name)))
                elif ext in archive:
                    os.makedirs(f'{paths}/압축 파일', exist_ok=True)
                    shutil.move(i, os.path.join(f'{paths}/압축 파일', os.path.basename(Path(i).name)))
                elif ext in web:
                    os.makedirs(f'{paths}/웹코드', exist_ok=True)
                    shutil.move(i, os.path.join(f'{paths}/웹코드', os.path.basename(Path(i).name)))
                elif ext in data:
                    os.makedirs(f'{paths}/데이터 파일', exist_ok=True)
                    shutil.move(i, os.path.join(f'{paths}/데이터 파일', os.path.basename(Path(i).name)))
                elif ext in text:
                    os.makedirs(f'{paths}/텍스트', exist_ok=True)
                    shutil.move(i, os.path.join(f'{paths}/텍스트', os.path.basename(Path(i).name)))
                else:
                    if f'{os.sep}{Path(Path(i).name).suffix}' not in Path(i).name:
                        os.makedirs(f'{paths}/{Path(Path(i).name).suffix}', exist_ok=True)
                        shutil.move(i,os.path.join(f'{paths}/{Path(Path(i).name).suffix}', os.path.basename(Path(i).name)))
            except:
                continue
        elif os.path.isdir(i):
            if any(os.path.isfile(os.path.join(i,file)) for file in os.listdir(i)):
                if os.path.basename(i) not in ['폴더', '사진', '동영상', '텍스트', '코드', '데이터', '웹코드', '각종 문서', '압축 파일', '음악과 음향',f'{Path(Path(i).name).suffix}']: # '폴더' 폴더 옮기기 X
                    os.makedirs(os.path.join(paths, '폴더'), exist_ok=True)
                    shutil.move(i, os.path.join(paths, '폴더', os.path.basename(i)))


if __name__ == "__main__":
    read = allread('dist/파일정리기/live_c.log').split('\n')
    print(f"감시 시작 대상 폴더: {len(read)}개")
    try:
        while True:
            for t in read:
                watch(t)
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n사용자가 프로그램을 종료했습니다.")