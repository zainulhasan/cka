#!/usr/bin/env python3
"""Regenerate guide/_sidebar.md from the backlog + lesson files that exist. Run after lessons land."""
import re, pathlib
G = pathlib.Path(__file__).resolve().parent.parent
backlog = (G/"inputs/TOPIC-BACKLOG.md").read_text()
titles = re.findall(r"^### (T(\d)\.\d\d) (.+)$", backlog, re.M)
dirs = {"1":"part1-linux","2":"part2-basics","3":"part3-ckad","4":"part4-cka"}
names = {"1":"Part 1 - Linux for Kubernetes","2":"Part 2 - Kubernetes basics","3":"Part 3 - CKAD","4":"Part 4 - CKA"}
out = ["* [Home](README.md)", "* [Conventions](00-conventions.md)", "* [Progress](PROGRESS.md)"]
for part in "1234":
    out.append(f"* {names[part]}")
    for tid, p, title in titles:
        if p != part: continue
        f = next((x for x in (G/dirs[p]).glob(f"{tid}-*.md")), None)
        out.append(f"  * [{tid} {title}]({dirs[p]}/{f.name})" if f else f"  * {tid} {title} (not written yet)")
(G/"_sidebar.md").write_text("\n".join(out)+"\n")
print(f"sidebar: {sum('not written' not in l and l.startswith('  *') for l in out)} lessons linked")
