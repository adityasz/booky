#!/usr/bin/env python3
import sys

level = 0
offset = 0

level_start_char = "{"
level_end_char = "}"
offset_char = '!'

for line in sys.stdin:
    line = line.strip()
    if line == level_start_char:
        level += 1
    elif line == level_end_char:
        level -= 1
    elif line[0] == offset_char and line.lstrip('-!').isdigit():
        offset = int(line[1:])
    elif line:
        comma_index = line.rfind(',')
        title = line[:comma_index].strip()
        pageNo = int(line[comma_index + 1:].strip()) + offset
        print("BookmarkBegin")
        print("BookmarkTitle:", title)
        print("BookmarkLevel:", level)
        print("BookmarkPageNumber:", pageNo)
