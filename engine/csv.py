from .base import *
from .files import *


def csv_parse_line(header: str, line: str) -> dict:
  header_lst = map(str.strip, header.strip().split(','))
  line_lst = map(str.strip, line.strip().split(','))
  return dict(zip(header_lst, line_lst ))


def csv_read(filename: str) -> list:
  if file_is_empty(filename, EXT_CSV, False):
    return []
  else:
    lines = file_read_lines(filename, EXT_CSV, False)
    header = lines.pop(0)
    result = []
    for line in lines:
      result.append(csv_parse_line(header, line))
    return result


def csv_try_write_header(filename: str, entity: dict):
  if not file_exists(filename, EXT_CSV, False):
    file_create(filename, EXT_CSV, False)
  if file_is_empty(filename, EXT_CSV, False):
    header = ','.join(entity.keys())
    file_write_line(filename, header, EXT_CSV, False)


def csv_write_entity(filename: str, entity: dict):
  csv_try_write_header(filename, entity)
  file_write_line(filename, ','.join(str(value) for value in entity.values()), EXT_CSV, False)


def csv_rewrite(filename: str, entities: list):
  file_erase(filename, EXT_CSV, False)
  for entity in entities:
    csv_write_entity(filename, entity)


def csv_check_unique(filename: str, entity: dict, checked_field: str) -> bool:
  if not file_exists(filename, EXT_CSV, False):
    raise FileNotFoundError(f"File {filename} not found. Try again.")
  stringified_entities = csv_read(filename)
  for str_entity in stringified_entities:
    if str_entity[checked_field] == str(entity[checked_field]):
      return False
  return True


def csv_autoincrement_id(name: str) -> int|None:
  ids = csv_read(FILE_NAMES["IDS"])
  if name not in ids[0].keys():
    return None
  ids[0][name] = int(ids[0][name]) + 1
  csv_rewrite(FILE_NAMES["IDS"], ids)
  return ids[0][name]


def csv_write_billing(entity: dict):
  entity_to_write = {"id": 0, "patient_id": 0, "service_id": 0, "total": 0, "paid": 0, "date": ""}
  entity_to_write.update(entity)
  entity_to_write["id"] = csv_autoincrement_id("billing")
  csv_write_entity(FILE_NAMES["BILLING"], entity_to_write)
  return entity_to_write["id"]


def csv_write_medical_history(entity: dict):
  entity_to_write = {"id": 0, "patient_id": 0, "action": "", "date": "", "notes": "", "HR": 0, "SYS": 0, "DIA": 0}
  entity_to_write.update(entity)
  entity_to_write["id"] = csv_autoincrement_id("medical_history")
  csv_write_entity(FILE_NAMES["MEDICAL_HISTORY"], entity_to_write)
  return entity_to_write["id"]


def csv_write_doctor(entity: dict):
  entity_to_write = {"id": 0, "user_id": 0, "name": "", "number": "", "address": ""}
  entity_to_write.update(entity)
  entity_to_write["id"] = csv_autoincrement_id("doctor")
  csv_write_entity(FILE_NAMES["DOCTORS"], entity_to_write)
  return entity_to_write["id"]


def csv_write_medication_log(entity: dict):
  entity_to_write = {"id": 0, "name": "", "date": "", "status": ""}
  entity_to_write.update(entity)
  entity_to_write["id"] = csv_autoincrement_id("medication_log")
  csv_write_entity(FILE_NAMES["MEDICATION_LOGS"], entity_to_write)
  return entity_to_write["id"]


def csv_write_patient(entity: dict):
  entity_to_write = {"id": 0, "user_id": 0, "name": "", "address": "", "age": 0, "phone_number": "", "diagnosis": "", "prescription": "", "treatment_plan": "", "status": ""}
  entity_to_write.update(entity)
  entity_to_write["id"] = csv_autoincrement_id("patient")
  csv_write_entity(FILE_NAMES["PATIENTS"], entity_to_write)
  return entity_to_write["id"]


def csv_write_room_prep(entity: dict):
  entity_to_write = {"id": 0, "user_id": 0, "description": "", "room_id": ""}
  entity_to_write.update(entity)
  entity_to_write["id"] = csv_autoincrement_id("room_prep")
  csv_write_entity(FILE_NAMES["ROOM_PREP"], entity_to_write)
  return entity_to_write["id"]


def csv_write_service(entity: dict):
  entity_to_write = {"id": 0, "doctor_id": 0, "patient_id": 0, "date": "", "description": "", "status": "", "is_appointment": False}
  entity_to_write.update(entity)
  entity_to_write["id"] = csv_autoincrement_id("service")
  csv_write_entity(FILE_NAMES["SERVICES"], entity_to_write)
  return entity_to_write["id"]


def csv_write_user(entity: dict):
  entity_to_write = {"id": 0, "email": "", "password": "", "role": "", "registration_date": ""}
  entity_to_write.update(entity)
  entity_to_write["id"] = csv_autoincrement_id("user")
  csv_write_entity(FILE_NAMES["USERS"], entity_to_write)
  return entity_to_write["id"]
