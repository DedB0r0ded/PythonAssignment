from .base import *
from .files import *


def csv_parse_line(header: str, line: str) -> dict:
  return dict(zip(header.strip().split(','), line.strip().split(',')))


def csv_read(filename: str) -> list:
  if file_is_empty(filename, EXT_CSV):
    return []
  else:
    lines = file_read_lines(filename, EXT_CSV)
    header = lines.pop(0)
    result = []
    for line in lines:
      result.append(csv_parse_line(header, line))
    return result


def csv_write_entity(filename: str, entity: dict):
  if not file_exists(filename, EXT_CSV):
    file_create(filename, EXT_CSV)
  if file_is_empty(filename, EXT_CSV):
    header = ','.join(entity.keys())
    file_write_line(filename, header, EXT_CSV)
  file_write_line(filename, ','.join(str(value) for value in entity.values()), EXT_CSV)


def csv_check_unique(filename: str, entity: dict, checked_field: str) -> bool:
  if not file_exists(filename, EXT_CSV):
    raise FileNotFoundError(f"File {filename} not found. Try again.")
  stringified_entities = csv_read(filename)
  for str_entity in stringified_entities:
    if str_entity[checked_field] == str(entity[checked_field]):
      return False
  return True