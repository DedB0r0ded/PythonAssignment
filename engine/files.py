from .base import *


# =============____FILES____=============
def str_add_extension(filename: str, extension: str, add_extension: bool) -> str:
  """
  Adds extension to the end of the file name.
  :param filename: file name without extension.
  :param extension: string. File extension. If empty, '.txt' will be used.
  """
  if add_extension:
    if extension:
      return filename + '.' + extension.strip()
    return filename + ".txt"
  else:
    return filename


def file_exists(filename: str, extension: str = "", add_extension: bool = True) -> bool:
  filename_full: str = ""
  filename_full = str_add_extension(filename, extension, add_extension)
  try:
    with open(filename_full, 'r') as f:
      return True
  except FileNotFoundError:
    return False


def file_create(filename: str, extension: str = "", add_extension: bool = True):
  """
  Creates an empty text file if it doesn't exist.
  :param extension: string. File extension. If empty, '.txt' will be used.
  :param filename: string. File name without extension.
  :return: True if file was created successfully, else False
  """
  filename_full = str_add_extension(filename, extension, add_extension)
  if file_exists(filename, extension):
    return False
  else:
    with open(filename_full, 'w') as f:
      return True


def file_read_str(filename: str, extension: str = "", add_extension: bool = True) -> str:
  """
  Reads the whole file as one string if file exists.
  :param extension: string. File extension. If empty, '.txt' will be used.
  :param filename: string. File name without extension.
  :return: string. File contents as a string.
  """
  filename_full = str_add_extension(filename, extension, add_extension)
  try:
    with open(filename_full, 'r') as f:
      return f.read()
  except FileNotFoundError:
    print(f'File \"{filename_full}\" not found. Please check the file path.')


def file_read_lines(filename: str, extension: str = "", add_extension: bool = True) -> list:
  """
  Reads the file line by line if file exists.
  :param extension: string. File extension. If empty, '.txt' will be used.
  :param filename: string. File name without extension.
  :return: list of strings. File contents as a list of lines.
  """
  filename_full = str_add_extension(filename, extension, add_extension)
  try:
    with open(filename_full, 'r') as f:
      return [line.strip() for line in f.readlines()]
  except FileNotFoundError:
    print(f'File \"{filename_full}\" not found. Please check the file path.')


def file_write_str(filename: str, content: str, extension: str = "", add_extension: bool = True) -> bool:
  """
  Adds a string to the end of the file. Creates a new file if it doesn't exist.
  :param extension: string. File extension. If empty, '.txt' will be used.
  :param filename: string. File name without extension.
  :param content: string to be appended to the end of the file.
  :return: True if string was written successfully, else False.
  """
  with open(str_add_extension(filename, extension, add_extension), 'a') as f:
    f.write(content)
    return True


def file_write_line(filename: str, content: str, extension: str = "", add_extension: bool = True) -> bool:
  """
  Adds a string and a new line to the end of the file. Creates a new file if it doesn't exist.
  :param extension: string. File extension. If empty, '.txt' will be used.
  :param filename: string. File name without extension.
  :param content: string to be appended to the end of the file.
  :return: True if string was written successfully, else False.
  """
  return file_write_str(filename, content + "\n", extension, add_extension)


def file_erase(filename: str, extension: str = "", add_extension: bool = True):
  """
    Erases the file content.
    :param extension: string. File extension. If empty, '.txt' will be used.
    :param filename: string. File name without extension.
    """
  with open(str_add_extension(filename, extension, add_extension), 'w') as f:
    f.close()

def file_is_empty(filename: str, extension: str = "", add_extension: bool = True) -> bool:
  filename_full = str_add_extension(filename, extension, add_extension)
  try:
    with open(filename_full, 'r') as f:
      return len(f.readlines()) == 0
  except FileNotFoundError:
    print(f'File \"{filename_full}\" not found. Please check the file path.')