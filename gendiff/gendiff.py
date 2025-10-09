import json

def read_json(path):
    return json.load(open(path))

def generate_diff(path1, path2):
    data1 = read_json(path1)
    data2 = read_json(path2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = []

    for key in all_keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key in data1 and key not in data2:
            lines.append(f"- {key}: {val1}")
        elif key not in data1 and key in data2:
            lines.append(f"+ {key}: {val2}")
        elif val1 != val2:
            lines.append(f"- {key}: {val1}")
            lines.append(f"+ {key}: {val2}")
        else:
            lines.append(f"  {key}: {val1}")
    
    return "{\n" + "\n".join(lines) + "\n}"