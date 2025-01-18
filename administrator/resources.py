import engine as e


def init_resource_file():
  e.csv_try_write_header(e.FILE_NAMES["RESOURCES"], {"beds": 0, "facility": 0})


def resources_add_bed():
  resources = e.csv_read(e.FILE_NAMES["RESOURCES"])[0]
  resources["beds"] += 1
  e.csv_rewrite(e.FILE_NAMES["RESOURCES"], resources)


def resources_add_facility():
  resources = e.csv_read(e.FILE_NAMES["RESOURCES"])[0]
  resources["facility"] += 1
  e.csv_rewrite(e.FILE_NAMES["RESOURCES"], resources)


def resources_remove_bed():
  resources = e.csv_read(e.FILE_NAMES["RESOURCES"])[0]
  resources["beds"] -= 1
  e.csv_rewrite(e.FILE_NAMES["RESOURCES"], resources)


def resources_remove_facility():
  resources = e.csv_read(e.FILE_NAMES["RESOURCES"])[0]
  resources["facility"] -= 1
  e.csv_rewrite(e.FILE_NAMES["RESOURCES"], resources)
