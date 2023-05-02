import os

ds = {1:"chrome.exe", 2:"notepad", 3:"camera", 4:"winword", 5:"excel", 6:"powerpnt", 7:"mspaint",
    8:"C:\\Users\\thanh\\AppData\\Local\\Programs\\Zalo\\Zalo.exe", 9:"explorer",
    10:"C:\\Program Files\\WindowsApps\\FACEBOOK.317180B0BB486_1530.18.110.0_x64__8xx8rvfyw5nnt\\app\\Messenger.exe",
    11:"C:\\Users\\thanh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"}
nhap = int(input())
if nhap != 3:
    os.startfile(ds[nhap])
else:
    os.system(f'cmd /k "start microsoft.windows.{ds[nhap]}:"')