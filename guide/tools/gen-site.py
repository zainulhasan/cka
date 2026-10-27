#!/usr/bin/env python3
"""Regenerate guide/_sidebar.md and guide/ROADMAP.md from the backlog, PROGRESS.md and the lesson files that exist."""
import re, pathlib
G = pathlib.Path(__file__).resolve().parent.parent
backlog = (G/"inputs/TOPIC-BACKLOG.md").read_text()
progress = (G/"PROGRESS.md").read_text()
topics = re.findall(r"^### (T(\d)\.\d\d) (.+)$", backlog, re.M)
dirs = {"1":"part1-linux","2":"part2-basics","3":"part3-ckad","4":"part4-cka"}
names = {"1":"Part 1 - Linux for Kubernetes","2":"Part 2 - Kubernetes basics","3":"Part 3 - CKAD","4":"Part 4 - CKA"}
status = {m.group(1): m.group(2).strip() for m in re.finditer(r"^\| (T\d\.\d\d) \|.*\| ([A-Z-]+)[^|]*\|[^|]*\|$", progress, re.M)}
hours = {}
for m in re.finditer(r"^### (T\d\.\d\d) .*?\n- Part / order / estimated study hours: .*?/ ([\d.]+) h", backlog, re.M):
    hours[m.group(1)] = m.group(2)

def lesson(tid, p):
    return next((x for x in (G/dirs[p]).glob(f"{tid}-*.md")), None)

side = ["* [Home](README.md)", "* [Roadmap: all 76 topics](ROADMAP.md)", "* [Conventions](00-conventions.md)", "* [Progress](PROGRESS.md)"]
road = ["# Roadmap", "", "All 76 topics in learning order. Written lessons are links; the rest are planned.", ""]
for part in "1234":
    pt = [t for t in topics if t[1] == part]
    done = [t for t in pt if lesson(t[0], part)]
    side.append(f"* {names[part]} ({len(done)} of {len(pt)} written)")
    road += [f"## {names[part]}", "", "| ID | Topic | Hours | Status |", "|---|---|---|---|"]
    for tid, _, title in pt:
        f = lesson(tid, part)
        st = status.get(tid, "")
        tag = {"PASS": "ready", "NEEDS-HUMAN": "written, has a known error"}.get(st, "written" if f else "not written yet")
        if f:
            side.append(f"  * [{tid} {title}]({dirs[part]}/{f.name}){' [needs fix]' if st == 'NEEDS-HUMAN' else ''}")
            road.append(f"| {tid} | [{title}]({dirs[part]}/{f.name}) | {hours.get(tid, '')} | {tag} |")
        else:
            road.append(f"| {tid} | {title} | {hours.get(tid, '')} | {tag} |")
    road.append("")
(G/"_sidebar.md").write_text("\n".join(side)+"\n")
(G/"ROADMAP.md").write_text("\n".join(road))
print(f"{sum(1 for t in topics if lesson(t[0], t[1]))} of {len(topics)} lessons written; status parsed for {len(status)}")
