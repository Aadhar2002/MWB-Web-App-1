FILEPATH = "chores_list.rtf"

def get_chores(filepath=FILEPATH):
  """
  Reads the text file and prints the list of chores.
  """
  with open(filepath, 'r') as file_local:
    chores_local = file_local.readlines()
  return chores_local


def write_chores(chores_arg, filepath=FILEPATH):
  """
  Writes the items in chores list
  """
  with open(filepath, 'w') as file:
    file.writelines(chores_arg)