import platform

import toml

def replace_os_path_sep():
    os_name = platform.system()
    if os_name in  ["Linux", "Darwin"]:
        return "/", "/"
    else:
        return "/", "\\"

    
def reader_config():
    old_sep, new_sep = replace_os_path_sep()
    with open('../config.toml'.replace(old_sep, new_sep), 'w') as f:
        new_toml_string = toml.load(f)
    return new_toml_string