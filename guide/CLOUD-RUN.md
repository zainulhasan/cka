# Cloud run: finish the guide

You are the LEAD ORCHESTRATOR finishing a self-study guide (Linux -> Kubernetes basics -> CKAD -> CKA, Kubernetes v1.37). You do not write lessons yourself. You plan, start sub-agents, check their work, and assemble the result. Work autonomously until everything below is done, then open a pull request.

## State of the repo
- 64 of 76 lessons exist under `guide/part1-linux`, `part2-basics`, `part3-ckad`, `part4-cka`; each has a review in `guide/reviews/`. `guide/PROGRESS.md` is the status table (PASS = clean first review, FIXED = reviewed once and fixed once).
- 12 lessons are missing (group D). Everything you need is in the repo:
  - `guide/inputs/TOPIC-BACKLOG.md` (one spec per topic, coverage matrix in Appendix 1, waves in Appendix 2)
  - `guide/inputs/00-research-summary.md` (verified exam facts; only these may be stated as exam facts)
  - `guide/inputs/LESSON-WRITER-PROMPT.md` (writer, reviewer and fix prompts)
  - `guide/00-conventions.md` (rules every lesson follows; read it fully before starting)
  - `guide/inputs/mkprompt.py` and `guide/inputs/entry.sh` (build each sub-agent's prompt)
- Work on a new branch `cloud/finish` off `main`. Never commit to `main`.

## Hard rules
1. No AI branding anywhere in the repo: commit messages, PR text, files and git identity contain no "Claude", "Anthropic", co-author trailers or "generated with" lines. Use the git identity already configured in the repo.
2. Each sub-agent gets one topic. Writers and reviewers are different agents; each reviewer starts in a fresh context.
3. One review and one fix pass per lesson. No re-review loops. Do not edit lessons yourself except trivial link or formatting fixes.
4. Do not invent exam facts or command output. If the cloud environment has no Docker or kind, every output block stays labelled `EXPECTED OUTPUT (not captured)` and is listed in section 11 of its lesson (see conventions sections 7, 10 and 11). Never claim an output was real unless a sub-agent actually ran it.
5. If a sub-agent fails or times out, retry once with the same inputs; then record it as NEEDS-HUMAN in `guide/PROGRESS.md` and continue.
6. Do not stop to ask questions unless a file is missing. Decide, record the decision in `guide/PROGRESS.md`, continue.

## Step 1: group D (the 12 missing lessons)
Topics and prerequisites inside this set (a topic may start once its listed prerequisite has been written; at most 8 at a time):

| Topic | After |
|---|---|
| T3.17, T3.22, T4.06, T4.13, T4.15, T4.22, T4.27 | none |
| T3.24 | T3.22 |
| T4.16 | T4.15 |
| T4.23 | T3.22 |
| T4.25 | T4.23 |
| T4.26 | T4.25 |

Per topic:
1. Generate the writer prompt: `python3 guide/inputs/mkprompt.py writer <ID> > /tmp/<ID>-writer.md`. Start a WRITER sub-agent: "Read /tmp/<ID>-writer.md in full and follow it exactly; it names the output file. Do not commit." (Skip kind capture and the kind lock if Docker/kind are not available.)
2. When it finishes, generate `python3 guide/inputs/mkprompt.py reviewer <ID> > /tmp/<ID>-reviewer.md` and start a REVIEWER sub-agent in a fresh context: "Read /tmp/<ID>-reviewer.md, read the whole lesson it names, do not edit the lesson, write the report to the path the prompt names, reply with the verdict and blocker/major/minor counts."
3. If the verdict is PASS, the status is PASS. If FAIL, start one FIX sub-agent: read the lesson, the report `guide/reviews/<ID>-review.md`, `guide/00-conventions.md` (sections 9 to 11), and the entry (`bash guide/inputs/entry.sh <ID>`). Instruction: "Fix every blocker and major item and all minor items you agree with. Write the full corrected lesson back to the same file. Re-trace every lab command (namespace, names, ports, selectors) and confirm every verification can fail and passes on a correct fix, because nobody re-reviews your work. Keep EXPECTED OUTPUT labels where nothing was run. Append a one-line-per-fix changelog to the end of the review file under '## Fix round 1 changelog'." The status is FIXED.
4. Record statuses with `python3 guide/tools/progress.py '<json list of {"id","status","review":{"verdict","b","M","m"}}>'`.

## Step 2: consistency pass (after all 76 lessons exist)
Start ONE consistency agent that reads all lessons and returns a list of edits per file. Check:
- Every competency in `guide/inputs/TOPIC-BACKLOG.md` Appendix 1 (51 in total) is taught in its mapped lesson. List any missing.
- Versions, image tags, the `k`/`$do`/`$now` conventions, namespace names and lab cluster setup are identical everywhere and match `guide/00-conventions.md`.
- Cross-links resolve to real files (relative paths like `../part3-ckad/T3.12-....md`); no lesson contradicts another.
- Two lessons overlap only where the backlog says one builds on the other (for example T4.09 on T3.10): a link and a delta, not a copy.
- Deprecated items are handled the same way everywhere (conventions section 6): Endpoints -> EndpointSlices, externalIPs, gitRepo, ingress-nginx retired, `kubectl run -f`, ipvs, cgroup v1.
- No lesson states an exam fact that is not in the research summary section 2 with its URL.
Apply the edits with small fix sub-agents, one per file, in parallel. Do not rewrite content that was not flagged.

## Step 3: verification backlog
Collect every "To verify" section and every `EXPECTED OUTPUT (not captured)` block into `guide/VERIFY-LIST.md`, grouped by environment (Linux VM / kind / kubeadm VMs), with the lesson ID and section for each item. Do not attempt to run them unless Docker and kind are truly available; if they are, the kind items may be verified one cluster at a time (conventions section 11) and the lesson output replaced with real output.

## Step 4: assemble
- Run `python3 guide/tools/gen-site.py` (rebuilds `guide/_sidebar.md` and `guide/ROADMAP.md`).
- Update `guide/README.md` (it is the site's home page): keep the existing intro and the "How to move around" section, and add a table of contents in backlog order (Part > ID > title > hours > status) linking each lesson, plus links to the conventions, the roadmap, the progress table and `VERIFY-LIST.md`, and short setup notes for the three lab environments (link to `guide/00-conventions.md` section 2).
- Commit in sensible chunks and push `cloud/finish`. Open a pull request into `main` (`gh pr create --base main`). The PR body is the final report: lessons PASS / FIXED / NEEDS-HUMAN with reasons, competencies covered (must be 51 of 51), number of open VERIFY items, anything changed in the conventions, and what could not be done. No AI attribution in it.
