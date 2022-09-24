import os


os.mkdir("FolderOfSecrets")
os.mkdir("/mnt/c/Users/bakti/OneDrive/Рабочий стол/Python Projects/testVirtualenv/FolderOfSecrets/FolderInFolder")

print(os.listdir('FolderOfSecrets'))
print("---")
text = os.open("FolderOfSecrets/text.txt", os.O_RDWR)
print(os.read(text, 12)) 


os.rmdir("/mnt/c/Users/bakti/OneDrive/Рабочий стол/Python Projects/testVirtualenv/FolderOfSecrets/FolderInFolder")

print("---")

print(os.listdir('FolderOfSecrets'))