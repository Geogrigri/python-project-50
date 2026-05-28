def stringify(value):
    if isinstance(value, dict):
        return "[complex value]"

    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return "null"

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)


def build_property_path(path, key):
    return ".".join([*path, key])


def iter_lines(diff, path=None):
    if path is None:
        path = []

    lines = []

    for node in diff:
        key = node["key"]
        node_type = node["type"]
        property_path = build_property_path(path, key)

        if node_type == "nested":
            lines.extend(iter_lines(node["children"], [*path, key]))

        elif node_type == "added":
            value = stringify(node["value"])
            lines.append(
                f"Property '{property_path}' was added with value: {value}"
            )

        elif node_type == "removed":
            lines.append(f"Property '{property_path}' was removed")

        elif node_type == "changed":
            old_value = stringify(node["old_value"])
            new_value = stringify(node["new_value"])
            lines.append(
                f"Property '{property_path}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return lines


def format_plain(diff):
    return "\n".join(iter_lines(diff))
