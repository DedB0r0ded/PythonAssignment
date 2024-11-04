def start_loop():
  pass


def file_create(filename: str):
  with open(filename, 'w') as f:
    pass

def file_read_str(filename: str) -> str:
  try:
    with open(filename, 'r') as f:
      return f.read()
  except FileNotFoundError:
    print('File not found. Please check the file path.')

def file_read_lines(filename: str) -> list:
  try:
    with open(filename, 'r') as f:
      return f.readlines()
  except FileNotFoundError:
    print('File not found. Please check the file path.')

def file_write_str(filename: str, content: str):
  with open(filename, 'a') as f:
    f.write(content)