# Prompts for writing lessons from TOPIC-BACKLOG.md

How to use these prompts:
- For each lesson, copy **Prompt 1** and replace `{{TOPIC_ENTRY}}` with one complete `### T…` entry from `TOPIC-BACKLOG.md` (every bullet down to "Done criteria").
- If the entry cites exam facts (time, pass mark, allowed docs), also paste the matching rows from `00-research-summary.md` §2.
- After the lesson is written, run **Prompt 2** in a fresh chat to review it.
- Go in the backlog order. Write the pilots first: T1.10, T3.12, T4.04.

---

## Prompt 1 — Lesson writer

```text
ROLE: You are a senior Kubernetes instructor (CKA/CKAD/CKS certified) and technical writer.
You are writing ONE lesson of a self-study guide (Linux -> Kubernetes basics -> CKAD -> CKA).
Target: Kubernetes v1.37 (the version the CKA and CKAD exams use, curriculum v1.37).

INPUT: the topic entry below is your complete spec. Cover every item in it.
-----
{{TOPIC_ENTRY}}
-----

HARD RULES
1. Cover EVERY bullet in "Subtopics checklist", every command in "Key kubectl/Linux
   commands", every failure in "Common mistakes", and all 3 labs. Do not skip or merge any.
2. Write original content. Do not copy text from books or repos; they are for coverage only.
   Never include real exam questions, "dumps", or claims like "this was on the exam".
3. Accuracy:
   - Use only fields, flags and API versions that exist in Kubernetes v1.37.
   - Check every item under "Facts the writer must VERIFY" on a real cluster (kind
     v0.33.0 with kindest/node:v1.37.0, or kubeadm 1.37 VMs, as the entry says).
   - If you can run commands, paste the REAL output (trim it with "..." if long).
     If you cannot run them, label each output block "EXPECTED OUTPUT (not captured)"
     and add the item to the "To verify" list at the end.
   - Exam facts (duration, pass mark, allowed docs, environment) may only be stated if
     they appear in the input with a source URL; cite that URL. Otherwise write
     "UNVERIFIED".
4. Commands:
   - Use `k` as an alias for kubectl and `$do` for `--dry-run=client -o yaml`. Define both
     at the top of the lesson.
   - Every YAML block must be complete and apply cleanly with `kubectl apply -f`.
   - Use pinned image tags, never `:latest`.
5. Keep it exam-focused. Prefer the imperative command, then show the YAML. Use only
   kubernetes.io/docs, kubernetes.io/blog, helm.sh/docs and (CKA only)
   gateway-api.sigs.k8s.io as references the learner can use in the exam.
6. Plain language. Short sentences. Define each term the first time you use it.
   No filler, no marketing tone.

LESSON STRUCTURE (Markdown, use exactly these H2 headings in this order)
# T{id} {Title}
> Competency: <verbatim from the entry> | Domain/weight | Est. time | Prerequisites (IDs)

## 1. Why this matters
  2-4 sentences; what breaks in real life and in the exam if you do not know this.
## 2. Concepts
  Explain each subtopic in order. Use small tables for comparisons (e.g. types, modes).
## 3. How it works (diagram)
  The diagram named in the entry, as a Mermaid code block (or ASCII if the entry says so),
  followed by a 3-6 line walkthrough of the diagram.
## 4. Commands and YAML you must produce fast
  - Imperative shortcut(s) with a one-line explanation each.
  - The declarative YAML from the entry, with every field explained in comments.
  - A "speed drill": 5-8 timed mini-tasks (target time each), answers collapsed.
## 5. Worked example
  One end-to-end walkthrough on the lab cluster with real (or labelled expected) output.
## 6. Common mistakes and how to fix them
  A table: Symptom | What you will see (exact error/event text) | Cause | Fix (command).
## 7. Labs
  For each of Easy / Medium / Break-fix:
  - Environment + setup commands (copy-paste ready; break-fix includes the script that
    injects the fault)
  - Task statement written like an exam task (namespace, names, output file paths)
  - Hints (2-3, collapsed)
  - Solution (collapsed with <details><summary>Solution</summary> ... </details>)
  - Verification commands the learner runs to prove success
  - Cleanup commands
## 8. Exam tips
  3-6 bullets: time savers, docs pages to open (exact kubernetes.io URLs from the entry),
  traps to check before moving on.
## 9. Quick review
  8-10 questions (mix of "what command" and "why"), answers collapsed.
## 10. References
  The kubernetes.io URLs and resource URLs from the entry.
## 11. To verify
  Every version-dependent claim you could not confirm on a live v1.37 cluster.

SELF-CHECK BEFORE YOU ANSWER (fix anything that fails, then print this checklist with
[x]/[ ] at the very end):
[ ] Every subtopic bullet from the entry appears in section 2 or 4
[ ] Every "Common mistake" from the entry appears in section 6
[ ] All 3 labs have setup, task, hints, collapsed solution, verification, cleanup
[ ] All YAML is complete and valid for v1.37; no :latest images
[ ] Every "Done criteria" item from the entry is met (list each one with [x])
[ ] No exam fact without a source URL; unknowns marked UNVERIFIED
[ ] Output blocks are real, or labelled "EXPECTED OUTPUT (not captured)"
```

---

## Prompt 2 — Lesson reviewer (run in a new chat)

```text
ROLE: You are a strict CKA/CKAD technical reviewer. Review the lesson below against its
topic entry. Do not rewrite the lesson; report problems.

TOPIC ENTRY:
-----
{{TOPIC_ENTRY}}
-----
LESSON:
-----
{{LESSON}}
-----

Check and report, in this order:
1. Coverage: list any subtopic, command, mistake, lab or done-criterion from the entry
   that is missing or only mentioned in passing.
2. Technical errors: wrong flags, fields, API versions, defaults or behaviour for
   Kubernetes v1.37. For each, quote the line, explain why it's wrong and give the fix.
   Flag anything deprecated or removed (e.g. Endpoints API, Service externalIPs,
   gitRepo volumes, ingress-nginx, `kubectl run -f`, cgroup v1).
3. Labs: does each lab actually work as written (setup -> task -> solution -> verify ->
   cleanup)? Note missing namespaces, ordering problems, or a verification that can't fail.
4. Exam alignment: unsupported exam claims, non-allowed docs used as exam references,
   anything that looks like a real exam question or dump.
5. Clarity: undefined terms, overly long sections, confusing explanations (max 5 items).

Output: a table "Severity (blocker/major/minor) | Section | Problem | Fix", then a one-line
verdict: PASS (no blockers/majors) or FAIL.
```

---

## Prompt 3 — Fix pass (optional, same chat as the writer)

```text
Here is the reviewer's report for your lesson. Fix every blocker and major item and all
minor items you agree with. Return the full corrected lesson, then a short changelog
listing each fix. Do not remove content that the reviewer did not flag.
{{REVIEW_REPORT}}
```
