#!/usr/bin/env python3
"""usage: mkprompt.py writer|reviewer|fix ID [lesson_path|review_path]  -> prints the agent prompt."""
import re, subprocess, sys, pathlib
here = pathlib.Path(__file__).parent
G = here.parent
backlog = (here/"TOPIC-BACKLOG.md").read_text()
prompts = (here/"LESSON-WRITER-PROMPT.md").read_text()
summary = (here/"00-research-summary.md").read_text()
conv = (G/"00-conventions.md").read_text()
blocks = re.findall(r"```text\n(.*?)\n```", prompts, re.S)  # Prompt 1, 2, 3
titles = dict(re.findall(r"^### (T\d\.\d\d) (.+)$", backlog, re.M))
partdir = {"1":"part1-linux","2":"part2-basics","3":"part3-ckad","4":"part4-cka"}
def slug(t): return "-".join(re.sub(r"[^a-z0-9 ]"," ",t.lower()).split()[:6])
def path(i): return f"{partdir[i[1]]}/{i}-{slug(titles[i])}.md"
def entry(i): return subprocess.check_output([str(here/"entry.sh"), i], text=True).strip()
def sec(n):
    m = re.search(rf"^## {n}\. .*?(?=^## \d+\. |^---\s*$)", summary, re.S|re.M); return m.group(0).strip()
def prereqs(i):
    m = re.search(r"Prerequisite topics \(IDs\): (.*)", entry(i)); return re.findall(r"T\d\.\d\d", m.group(1))

kind, i = sys.argv[1], sys.argv[2]
if kind == "writer":
    pre = "\n".join(f"- {p} {titles[p]} -> guide/{path(p)}" for p in prereqs(i)) or "(none)"
    print(blocks[0].replace("{{TOPIC_ENTRY}}", entry(i)))
    print(f"""

=== ADDITIONAL INPUTS ===
YOUR OUTPUT FILE: /Users/zain/projects/cka/guide/{path(i)}  (write the full lesson there with the Write tool, then reply with a 5-line summary and the self-check checklist).
ENVIRONMENT LIMITS: kind and multipass are NOT installed on this machine, so you cannot run cluster or VM labs. Label every such output block exactly "EXPECTED OUTPUT (not captured)" and list it in section 11. Docker is available if you want to test a plain Linux command in a container, but never claim it was a VM or kind result.
PREREQUISITES (cross-link to them, do not re-teach; the files may not exist yet, link anyway):
{pre}

=== 00-conventions.md (follow exactly) ===
{conv}

=== Research summary §2 (exam facts, with URLs) ===
{sec(2)}

=== Research summary §5 (pinned versions) ===
{sec(5)}
""")
elif kind == "reviewer":
    suf = sys.argv[3] if len(sys.argv) > 3 else ""
    rep = f"{i}-review{'-' + suf if suf else ''}.md"
    print(blocks[1].replace("{{TOPIC_ENTRY}}", entry(i)).replace("{{LESSON}}", f"[READ THE FILE: /Users/zain/projects/cka/guide/{path(i)}]"))
    print(f"""

=== ADDITIONAL INPUTS ===
Read the lesson file above with the Read tool (the whole file, in chunks with offset/limit if it is large). Also read /Users/zain/projects/cka/guide/00-conventions.md and check the lesson against it, including section 9 (depth: list shallow or list-only subtopics as MAJOR) and sections 10-11.
You cannot re-run commands. Blocks labelled as real captures: judge them for plausibility and internal consistency (paths, values, units), not as unverified. ACCEPTED LIMITATION: output blocks labelled exactly "EXPECTED OUTPUT (not captured)" that are listed in section 11 under a "Known limitation" paragraph (no live cluster or VM available) must NOT be raised as a major on their own. Everything else (wrong flags, wrong ports, checks that cannot fail or cannot pass, unsourced exam claims, missing entry items) is in scope.
Do not edit the lesson. Do not read any earlier review report for this topic.
Write your report to /Users/zain/projects/cka/guide/reviews/{rep} (table "Severity | Section | Problem | Fix", then a final line "VERDICT: PASS" or "VERDICT: FAIL") and reply with only the verdict and the number of blocker/major/minor items.
Exam facts may be checked against summary §2:
{sec(2)}
""")
elif kind == "fix":
    print(blocks[2].replace("{{REVIEW_REPORT}}", f"[READ THE FILE: {sys.argv[3]}]"))
    print(f"\nWrite the full corrected lesson back to /Users/zain/projects/cka/guide/{path(i)} and append the changelog at the end of /Users/zain/projects/cka/guide/reviews/{i}-review.md. Reply with the changelog only.")
