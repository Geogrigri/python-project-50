SPACES_COUNT = 4
SIGN_OFFSET = 2


def stringify(value, depth):
    if isinstance(value, dict):
        lines = ["{"]
        indent = " " * (depth * SPACES_COUNT)

        for key, item in sorted(value.items()):
            lines.append(
                f"{indent}    {key}: {stringify(item, depth + 1)}"
            )

        lines.append(f"{indent}}}")
        return "\n".join(lines)

    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return "null"

    return str(value)


def make_indent(depth, sign=" "):
    return " " * (depth * SPACES_COUNT - SIGN_OFFSET) + sign + " "


def iter_lines(diff, depth):
    lines = []

    for node in diff:
        key = node["key"]
        node_type = node["type"]

        if node_type == "added":
            lines.append(
                f"{make_indent(depth, '+')}{key}: "
                f"{stringify(node['value'], depth)}"
            )
        elif node_type == "removed":
            lines.append(
                f"{make_indent(depth, '-')}{key}: "
                f"{stringify(node['value'], depth)}"
            )
        elif node_type == "changed":
            lines.append(
                f"{make_indent(depth, '-')}{key}: "
                f"{stringify(node['old_value'], depth)}"
            )
            lines.append(
                f"{make_indent(depth, '+')}{key}: "
                f"{stringify(node['new_value'], depth)}"
            )
        elif node_type == "unchanged":
            lines.append(
                f"{make_indent(depth)}{key}: "
                f"{stringify(node['value'], depth)}"
            )
        elif node_type == "nested":
            lines.append(f"{make_indent(depth)}{key}: {{")
            lines.extend(iter_lines(node["children"], depth + 1))
            lines.append(" " * (depth * SPACES_COUNT) + "}")

    return lines


def format_stylish(diff):
    lines = ["{"]
    lines.extend(iter_lines(diff, 1))
    lines.append("}")
    return "\n".join(lines)
