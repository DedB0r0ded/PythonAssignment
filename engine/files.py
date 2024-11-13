from .base import *


# =============____FILES____=============
def str_add_extension_txt(filename: str) -> str:
  """Adds '.txt' to the end of the file name."""
  return filename + ".txt"


def file_create(filename: str) -> bool:
  """
  Creates an empty text file if it doesn't exist.
  :param filename:
  :return: True if file was created successfully, else False
  """
  try:
    with open(str_add_extension_txt(filename), 'r') as f:
      return False
  except FileNotFoundError:
    with open(str_add_extension_txt(filename), 'w') as f:
      return True


def file_read_str(filename: str) -> str:
  """
  Reads the whole file as one string if file exists.
  :param filename: string. File name without extension.
  :return: string. File contents as a string.
  """
  try:
    with open(str_add_extension_txt(filename), 'r') as f:
      return f.read()
  except FileNotFoundError:
    print('File not found. Please check the file path.')


def file_read_lines(filename: str) -> list:
  """
  Reads the file line by line if file exists.
  :param filename: string. File name without extension.
  :return: list of strings. File contents as a list of lines.
  """
  try:
    with open(str_add_extension_txt(filename), 'r') as f:
      return [line.strip() for line in f.readlines()]
  except FileNotFoundError:
    print('File not found. Please check the file path.')


def file_write_str(filename: str, content: str) -> bool:
  """
  Adds a string to the end of the file. Creates a new file if it doesn't exist.
  :param filename: string. File name without extension.
  :param content: string to be appended to the end of the file.
  :return: True if string was written successfully, else False.
  """
  with open(str_add_extension_txt(filename), 'a') as f:
    f.write(content)
    return True


def file_write_line(filename: str, content: str) -> bool:
  """
  Adds a string and a new line to the end of the file. Creates a new file if it doesn't exist.
  :param filename: string. File name without extension.
  :param content: string to be appended to the end of the file.
  :return: True if string was written successfully, else False.
  """
  return file_write_str(filename, content + "\n")
