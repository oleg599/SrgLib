from srg.output import serialize_srg
from srg.parser import parse_lines

with open('joined.srg') as file:
    lines = file.read().splitlines(keepends=False)

mappings = parse_lines(lines)