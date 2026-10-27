#!/usr/bin/env python3
"""usage: progress.py '<json results>'  -> adds/updates rows in PROGRESS.md from a workflow result list."""
import json, re, sys, pathlib
G = pathlib.Path(__file__).resolve().parent.parent
res = json.loads(sys.argv[1])
backlog = (G/"inputs/TOPIC-BACKLOG.md").read_text()
groups = json.loads((G/"inputs/groups.json").read_text())
wave = {t["id"]: t["wave"] for g in groups.values() for t in g}
title = dict(re.findall(r"^### (T\d\.\d\d) (.+)$", backlog, re.M))
p = G/"PROGRESS.md"; lines = p.read_text().splitlines()
idx = {m.group(1): i for i, l in enumerate(lines) if (m := re.match(r"\| (T\d\.\d\d) \|", l))}
last_row = max(idx.values())
for r in res:
    rv = r.get("review") or {}
    verdict = f"{rv.get('verdict','-')} ({rv.get('b',0)}B/{rv.get('M',0)}M/{rv.get('m',0)}m)" if rv else "-"
    fixes = 1 if r["status"] == "FIXED" else 0
    note = r.get("note", "") or ("reviewed once, fixed once, not re-checked" if r["status"] == "FIXED" else "")
    row = f"| {r['id']} | {title[r['id']]} | {wave.get(r['id'],'')} | wf | {verdict} | {fixes} | {r['status']} | {note} |"
    if r["id"] in idx: lines[idx[r["id"]]] = row
    else:
        last_row += 1; lines.insert(last_row, row)
p.write_text("\n".join(lines) + "\n")
print(f"updated {len(res)} rows")
