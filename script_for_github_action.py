import yaml

def parse_yaml(file_path):
    """
    Parses a YAML file and returns the content as a dictionary.

    :param file_path: Path to the YAML file
    :return: Dictionary containing the parsed YAML content
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def get_nested_keys(file_path):
    """
    Retrieves nested keys from a YAML file.

    :param file_path: Path to the YAML file
    :return: List of nested keys
    """
    data = parse_yaml(file_path)
    nested_keys = []

    def extract_keys(d, parent_key=''):
        for k, v in d.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            if isinstance(v, dict):
                extract_keys(v, new_key)
            else:
                nested_keys.append(new_key)

    extract_keys(data)
    return nested_keys


nest_keys = get_nested_keys(file_path="generic.yaml")

# Write the nested keys to a text file
with open("nested_keys.txt", "w") as file:
    file.writelines(key + "\n" for key in nest_keys)
