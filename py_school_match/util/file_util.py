import os.path
import uuid
import time


def gen_filepath(path_to_file, filename="", extension=None, unique_file=False):
    """Generates a filepath."""
    if extension is None:
        raise Exception("Invalid file extension")

    if path_to_file:
        os.makedirs(path_to_file, exist_ok=True)

    if unique_file or not filename:
        file = "{}_{}.{}".format(time.strftime("%Y%m%d-%H%M%S"), str(uuid.uuid4().hex), extension)
    else:
        file = "{}.{}".format(filename, extension)

    filepath = os.path.join(path_to_file, file)
    return filepath


def get_number_list_from_file(file):
    """Creates a list of numbers from a file (numbers are separated by \n)."""
    with open(file) as f:
        lines = [float(line.rstrip('\n')) for line in f]

    return lines
