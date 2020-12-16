
import json

def ls(string, width, fill=" "):
    string = '%s' % (string)
    length = len(string)
    utf8_length = len(string.encode('utf-8'))
    lhanzi = (utf8_length - length) / 2
    return string.ljust(width -  int(lhanzi), fill)

def print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))