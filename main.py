import os
import winreg
import configparser


def RemoveFolders(a_folders: list):
    if not a_folders:
        print('No folders to remove. Config file is ok?')    
    for folder in a_folders:
        if FolderExists(folder):
            RemoveFolder(folder)
        else:
            print(f"Folder {folder} doesn't exist.")
            
def FolderExists(a_folderPath: str) -> bool:
    if os.path.exists(a_folderPath) and os.path.isdir(a_folderPath):
        return True;
    return False;

'''
Removes folders, assuming that they are empty. If they aren't, then tries to
remove them as well.
'''
def RemoveFolder(a_folderPath: str):
    try:
        try:
            os.rmdir(a_folderPath)
            print(f"Empty folder {a_folderPath} deleted successfully.")
        except OSError as e:
            import shutil
            shutil.rmtree(a_folderPath)
            print(f"Folder {a_folderPath} deleted successfully.")
    except Exception as e:
        print(f"Error deleting {a_folderPath}: {e}")

def  RemoveWorkstationRegistry():
    try:
        key_path = r'SOFTWARE\testFolder'
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteKey(key, '')

        print(f"{key_path} deleted successfully.")
    except Exception as e:
        print(f"Error deleting {key_path}: {e}")
    finally:
        key.Close()


def RemoveRegistryKeys(a_keys: list):
    if not a_keys:
        print('No keys to remove. Config file is ok?')    
    for key in a_keys:
        if KeyExists(key):
            RemoveKey(key)
        else:
            print(f"Key {key} doesn't exist.")

def KeyExists(a_key: str) -> bool:
    pass

def RemoveKey(a_key: str):
    pass

def ParsePaths(a_file: str,  a_group: str) -> list:
    config = configparser.ConfigParser()
    try:
        config.read(a_file)
    except Exception as e:
        print(e)
        return []

    paths = []
    for key in config[a_group]:
        try:
            paths.append(config[a_group][key])
        except Exception as e:
            print(e)
            continue

    # print(paths, sep='\n')
    return paths

if __name__ == "__main__":
    RemoveFolders(ParsePaths('Folders.conf', 'WorkstationPaths'))
    # RemoveFolders(ParsePaths('Folders.conf', 'MySQLPaths')
    # RemoveRegistryKeys(ParsePaths('Registry.conf', 'Workstation')
    # RemoveRegistryKeys(ParsePaths('Registry.conf', 'MySQL')

    pass
