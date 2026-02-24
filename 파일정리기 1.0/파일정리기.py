from customtkinter import *
from tkinter import messagebox, filedialog
import os, shutil, time
from pathlib import *
import easyfile as e
import tempfile

# 모듈 개별설치 요구사항 : customtkinter, pywin32
# ------------------------------------- ai생성
sys_temps = [
    os.path.join(os.environ.get('SystemRoot'), "Temp"), # C:\Windows\Temp
    os.path.join(os.environ.get('SystemRoot'), "Prefetch"), # C:\Windows\Prefetch
    os.path.join(os.environ.get('SystemRoot'), "SoftwareDistribution", "Download") # 업데이트 잔해
]
import ctypes
import sys
shell32 = ctypes.windll.shell32
def is_admin():
    try:
        return shell32.IsUserAnAdmin()
    except:
        return False
if not is_admin():
    shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()
# ------------------------------------- ai생성
window = CTk()
window.geometry("300x300")
window.resizable(width=False, height=False)
window.configure(fg_color='#242424')

set_appearance_mode("dark")  # "light", "dark" 중 선택
set_default_color_theme("blue")

dirt = ""
Stopped = False
asdf=[]
temps = tempfile.gettempdir()
start_menu = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
if os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), "Google", "Chrome", "User Data", "Default", "Cache")):
    c_cache = os.path.join(os.environ.get('LOCALAPPDATA'), "Google", "Chrome", "User Data", "Default", "Cache")
else:
    c_cache = os.path.join(os.environ.get('LOCALAPPDATA'), "Microsoft", "Edge", "User Data", "Default", "Cache")
d_cache = os.path.join(os.getenv('APPDATA'), "discord", "Cache")
# ━━━━━━━━━━━━━━━━━━━━
picture = ['png', 'jpg', 'jpeg', 'bmp', 'webp', 'gif',
           'PNG', 'JPG', 'JPEG', 'BMP', 'WEBP', 'GIF']
musics = ['mp3', 'wav', 'ogg', 'sf2'
          'MP3', 'WAV', 'OGG', 'SF2']
video = ['mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv', 'webm',
         'MP4', 'MKV', 'AVI', 'MOV', 'WMV', 'FLV', 'WEBM']
documents = ['pdf', 'docx', 'doc', 'pptx', 'ppt', 'xlsx', 'xls', 'hwp', 'hwpx','cell', 'csv'
             'PDF', 'DOCX', 'DOC', 'PPTX', 'PPT', 'XLSX', 'XLS', 'HWP', 'HWPX', 'Cell', 'CSV']
data = ['json', 'xml', 'yaml', 'yml', 'csv', 'db', 'sql',
        'JSON', 'XML', 'YAML', 'YML', 'CSV', 'DB', 'SQL']
text = ['txt', 'log', 'md',
        'TXT', 'LOG', 'MD']
code = ['py', 'c', 'cpp', 'cc', 'cs', 'java', 'lua', 'rb', 'go', 'rs', 'swift', 'kt', 'dart', 'sh', 'bat', 'ps1', 'h', 'hpp',
        'PY', 'C', 'CPP', 'CC', 'CS', 'JAVA', 'LUA', 'RB', 'GO', 'RS', 'SWIFT', 'KT', 'DART', 'SH', 'BAT', 'PS1', 'H', 'HPP']
web = ['html', 'htm', 'css', 'js', 'ts', 'jsx', 'tsx',
       'HTML', 'HTM', 'CSS', 'JS', 'TS', 'JSX', 'TSX']
archive = ['zip', 'rar', '7z', 'tar', 'gz',
           'ZIP', 'RAR', '7Z', 'TAR', 'GZ']

def tree_and_files(lists:list,directory, p, failed:list):
    for i in lists:
        try:
            paths = os.path.join(directory, i)
            if Path(str(paths)).name in protected_files:
                continue
            if os.path.isfile(paths):
                os.remove(paths)
                p.progress_up(i)
            else:
                shutil.rmtree(paths)
        except OSError:
            failed.append(i)
category_map = {} # 딕셔너리를 만든 다음에 이걸로 분류를 해
for x in picture:   category_map[x] = '사진'
for x in musics:    category_map[x] = '음악과 음향'
for x in video:     category_map[x] = '동영상'
for x in documents: category_map[x] = '각종 문서'
for x in data:      category_map[x] = '데이터'
for x in text:      category_map[x] = '텍스트'
for x in code:      category_map[x] = '코드'
for x in web:       category_map[x] = '웹코드'
for x in archive:   category_map[x] = '압축 파일'

protected_files = [
    os.path.basename(__file__),
    'watch_loop_files.pyw',
    'live_c.log',
    '.venv',      # 가상환경 폴더 보호
    '_internal',  # 빌드 후 부속 폴더 보호
    '.idea',      # 파이참 설정 폴더 보호
    '.git'        # 깃 설정 폴더 보호
]

if os.path.exists(os.path.join(start_menu, 'watch_loop_files.exe')):
    if os.path.exists('watch_loop_files.exe'):
        shutil.move("watch_loop_files.exe", start_menu)

def auto(fold):
    if not dirt in e.allread('dist/파일정리기/live_c.log').strip('\n'):
        response = messagebox.askyesno("확인", "자동으로 폴더가 정리되게 하겠습니까?\nlive_c.txt에서 디렉토리를 제거하시면 취소 할 수 있습니다.")
        if response:
            messagebox.showinfo('성공','자동으로 확장자별로 해당 폴더가 정리될 것입니다.')
            e.listappend_file('dist/파일정리기/live_c.log', f'{fold}')
        else:
            pass
    else:
        pass

def on_btn():
    global dirt
    dirt = filedialog.askdirectory()
    path_list = []
    if dirt != "":
        messagebox.showinfo('완료', '정상적으로 폴더를 지정했습니다')
        for root, dirs, files in os.walk(dirt):
            for d in dirs:
                path_list.append(os.path.join(root, d))
            for i in files:
                path = os.path.join(root, i)
                path_list.append(path)
        return path_list
    return []


def ret():
    global Stopped
    Stopped = True

def ejected():
    global protected_files
    zxcv=filedialog.askdirectory()
    if zxcv in protected_files:
        messagebox.showerror('에러', '이미 추가된 폴더입니다')
    elif zxcv == "": return None
    elif zxcv == dirt:
        messagebox.showerror('에러', '정리할 폴더와 제외 폴더가 같습니다')
        return None
    else:
        protected_files.append(zxcv)
        messagebox.showinfo('완료', '제외 폴더 추가가 완료되었습니다.')
    return protected_files
class Progress:
    def __init__(self, names):
        self.progress_window = CTkToplevel(window)
        self.progress_window.geometry("250x150")
        self.progress_window.title("정리 진행률")
        self.progress_window.attributes("-topmost", True) # <- Ai 작성

        self.progress = CTkLabel(self.progress_window, text='정리 시작!', font=('맑은 고딕', 20))
        self.progress.grid(row=0, column=1)
        CTkButton(self.progress_window, text='닫기', command=ret).grid(row=2, column=0, sticky='ew')

        self.prog_bar = CTkProgressBar(self.progress_window, width=250)
        self.prog_bar.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky='ew')
        self.prog_bar.set(0)

        if len(names) > 0:
            self.ai_bad = 1/len(names)
        else:
            self.ai_bad = 0
        self.current=0
    def progress_up(self, i):
        self.current += self.ai_bad
        self.prog_bar.set(self.current)
        self.progress.configure(text=f'{i} 처리 중')
        self.progress_window.update()

def files_be_better():
    global Stopped
    failed = []
    names = on_btn()
    try:
        Stopped = False
        progress = Progress(names)
        for i in names:
            try:
                window.update()
                if os.path.basename(i) in protected_files or i in protected_files:
                    continue
                if Stopped:
                    progress.progress.configure(text='중단!')
                    time.sleep(1)
                    progress.progress_window.destroy()
                    break
                elif not Stopped:
                    all_stars = i
                    if os.path.dirname(all_stars) != dirt:
                        continue
                    if os.path.isdir(all_stars):
                        if os.path.basename(i) not in ['폴더', '사진', '동영상', '텍스트', '코드', '데이터', '웹코드', '각종 문서', '압축 파일', '음악과 음향',f'{Path(Path(i).name).suffix}']: # '폴더' 폴더 옮기기 X
                            os.makedirs(os.path.join(dirt, '폴더'), exist_ok=True)
                            shutil.move(all_stars, os.path.join(dirt, '폴더', os.path.basename(all_stars)))
                            continue
                    if os.path.isfile(all_stars):
                        ext = i.lower().split('.')[-1]
                        f = category_map.get(ext, '기타항목') # 확장자가 아니면 기타항목으로 따로분류

                        target_path = os.path.join(dirt, f) # 확장자에 대한 폴더이름
                        os.makedirs(target_path, exist_ok=True) # 폴더만들기
                        shutil.move(i, os.path.join(target_path, os.path.basename(i))) # 이동
                        if category_map.get(ext, '기타항목') == '기타항목': # 따로처리할것
                            if f'{Path(all_stars).suffix}' not in all_stars:
                                os.makedirs(f'{dirt}/{Path(all_stars).suffix}', exist_ok=True)
                                shutil.move(all_stars, os.path.join(f'{dirt}/{Path(all_stars).suffix}', os.path.basename(all_stars)))
                        progress.progress_up(i)
            except (FileNotFoundError, PermissionError, IndexError) as er:
                failed.append(os.path.basename(i))
                if isinstance(er, FileNotFoundError):
                    messagebox.showwarning('일부 처리 실패',f'{os.path.basename(i)}가 존재하지 않습니다')
                elif isinstance(er, PermissionError):
                    messagebox.showwarning('일부 처리 실패', f'{os.path.basename(i)} 를 이동할 권한이 없습니다.')
                elif isinstance(er, IndexError):
                    messagebox.showwarning('일부 처리 실패', f'{os.path.basename(i)} 처리하지 못했습니다')
                pass
        if not failed:
            messagebox.showinfo('끝', '파일 정리를 했습니다!')
        else:
            messagebox.showinfo('끝', f'{failed} 실패! 타 파일 정리 성공')
        auto(dirt)
        window.update()
    except:
        pass

def sizer():
    labeltext = '사이즈 확인 중!'
    count = 0
    progress_window = CTkToplevel(window)
    progress_window.geometry("400x800")
    progress_window.attributes("-topmost", True)  # <- Ai 작성
    progress = CTkLabel(progress_window, text=labeltext, font=('맑은 고딕', 15), justify="left", wraplength=350)
    progress.grid(row=0, column=0, padx=10, pady=10)
    # ------------------------------------------------
    names = on_btn()
    big_list = ""
    limit = 1024 * 1024 * 1024
    for i in names:
        if os.path.isfile(i):
            size = os.path.getsize(i)
            if size > limit:
                big_list += f'{os.path.basename(i)} - 용량:{format(size / 1024 / 1024 / 1024, ".2f")} GB\n'
                count += 1
    if count > 0:
        progress.configure(text=big_list)
    else:
        progress.configure(text="1GB+ 파일이 존재하지 않는다.")

def remove_temp():
    failed = []
    temp_list = os.listdir(temps)
    if not temp_list:
        messagebox.showwarning('실패', '임시 파일이 존재하지 않습니다.')
        return
    chrome_list = os.listdir(c_cache)
    p = Progress(temp_list)

    tree_and_files(temp_list, temps, p, failed)
    what = messagebox.askyesno('작업 중', '''크롬 캐시 데이터를 지우시겠어요?\n
     크롬 이용이 조금 느려질 수 있습니다.''')
    if what:
        p.prog_bar.set(0)
        tree_and_files(chrome_list, c_cache, p, failed)
        if failed:
            failed_txt = '\n'.join(list(set(failed)))
            p.progress.configure(text=f'완료되었지만..\n 처리 불가 항목 \n {[failed_txt]}')
        else:
            p.progress.configure(text='완료되었습니다!', font=('맑은 고딕', 30))
    else:
        if failed:
            failed_txt = '\n'.join(list(set(failed)))
            p.progress.configure(text=f'완료되었지만..\n 처리 불가 항목 \n {[failed_txt]}')
        else:
            p.progress.configure(text='완료되었습니다!', font=('맑은 고딕', 30))
def end_progress():
    window.destroy()
    window.quit()
    exit()

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
import locale
l = locale.getlocale(locale.LC_CTYPE)[0]
if l.lower().startswith('ko'):
    CTkLabel(window, text = '튜브냥의 파일 정리기', font = ('Pretendard Bold', 25)). grid(row=0, column=0, padx=10, columnspan=3, pady=20, sticky='ew')
    CTkButton(window, text="폴더를\n정리하기", font=("Pretendard Bold", 15), command=files_be_better).grid(row=1, column=0, columnspan=1,sticky='ew', padx=10,pady=10)
    CTkButton(window, text="프로그램 종료하기", font=("Pretendard Bold", 15), command=end_progress).grid(row=3, column=0, columnspan=3,sticky='ew', padx=10, pady=10)
    CTkButton(window, text="대용량\n파일 보기", font=("Pretendard Bold", 15), command=sizer).grid(row=1, column=1, columnspan=1, sticky='ew',padx=10, pady=10)
    CTkButton(window, text="특정 폴더\n제외하기", font=("Pretendard Bold", 15), command=ejected).grid(row=1, column=2, columnspan=1,sticky='ew', padx=10, pady=10)
    CTkButton(window, text = '임시 파일 \n 삭제하기', font=('Pretendard Bold', 15), command=remove_temp).grid(row=2, column=0, columnspan=1, sticky='ew', padx=10, pady=10)
else:
    CTkLabel(window, text='File Organizer', font=('Pretendard Bold', 25)).grid(row=0, column=0,
                                                                               padx=10, columnspan=3,pady=20, sticky='ew')
    CTkButton(window, text="Organize\nFolders", font=("Pretendard Bold", 15), command=files_be_better).grid(row=1,column=0,
                                                                                                            columnspan=1,sticky='ew',padx=10,pady=10)
    CTkButton(window, text="Exit Program", font=("Pretendard Bold", 15), command=end_progress).grid(row=3, column=0
                                                                                                    ,columnspan=3,sticky='ew',padx=10, pady=10)
    CTkButton(window, text="Large\nFiles", font=("Pretendard Bold", 15), command=sizer).grid(row=1, column=1,
                                                                                             columnspan=1, sticky='ew',padx=10, pady=10)
    CTkButton(window, text="Exclude\nFolders", font=("Pretendard Bold", 15), command=ejected).grid(row=1, column=2,
                                                                                                   columnspan=1,sticky='ew', padx=10,pady=10)
    CTkButton(window, text='Clear\nTemp Files', font=('Pretendard Bold', 15), command=remove_temp).grid(row=2, column=0,
                                                                                                        columnspan=1,sticky='ew',padx=10,pady=10)

window.mainloop()
