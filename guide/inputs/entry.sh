#!/usr/bin/env bash
# usage: entry.sh T1.10  -> prints that topic's full entry from TOPIC-BACKLOG.md
awk -v id="### $1 " 'index($0,id)==1{p=1;print;next} p&&(/^### T[0-9]/||/^## /){exit} p' "$(dirname "$0")/TOPIC-BACKLOG.md"
