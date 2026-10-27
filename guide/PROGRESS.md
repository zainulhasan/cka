# PROGRESS (source of truth; resume from here)

Decisions:
- 2026-10-27: Inputs copied to guide/inputs/. `inputs/entry.sh <ID>` prints one topic entry.
- Part 2 directory is `part2-basics`. Env scripts live in guide/env/ (unverified until step 5).
- Step 1 done (00-conventions.md written).

| ID | Title | Wave | Writer | Review verdict | Fix rounds | Status | Open "To verify" items |
|---|---|---|---|---|---|---|---|
| T1.10 | Linux namespaces and cgroups v2 | 3 | a5ab984 | PASS (r1: 1 blocker, 5 major; r2: 5 major; r3: 0 major, 7 minor) | 2 | PASS | Real kind v0.33.0/v1.37.0 + Docker output captured; open: kubeadm node, Ubuntu VM and cgroup v1 node runs (section 11) |
| T3.12 | Provide and troubleshoot access to applications via Services | 9 | a2350d7 | FAIL (r1: 1 major; r2: 3 major; r3: 1 blocker, 1 major) | 2 | NEEDS-HUMAN | Open blocker (reviews/T3.12-review-r3.md): medium lab calls `db-0.db-hl:80`, but a headless Service does no port translation, so the client must use the Pod port 8080; lesson never explains this. Plus ~14+17 expected-output items |
| T4.04 | Manage the lifecycle of Kubernetes clusters | 7 | a449d04 | FAIL (r1: 4 major; r2: 3 major; r3: 1 major) | 2 | NEEDS-HUMAN | Open major (reviews/T4.04-review-r3.md): Lab C cert check (lines ~1380-1384) counts >=12 `NNNd` values, but a correct cluster shows 11 (CA rows print in years, e.g. 9y), so the check fails after a correct fix. ~25 verify items, no live VM capture |

Decisions (cont.):
- 2026-10-27: Re-reviews write to reviews/<ID>-review-r<N>.md so fix changelogs are not overwritten.
- 2026-10-27: T3.12 marked NEEDS-HUMAN after 2 fix rounds (rule: max 2). The remaining blocker is a one-line factual fix (headless Service port); left for a human per the no-edit-by-orchestrator rule.
- 2026-10-27: T4.04 marked NEEDS-HUMAN after 2 fix rounds. Remaining major is a one-line threshold fix (12 -> 11 or parse years too).
- 2026-10-27: Pilot round done: T1.10 PASS; T3.12, T4.04 NEEDS-HUMAN. The T1.10 writer ran a real kind cluster (downloaded the kind binary), so kind-topic writers may capture real output under the lock rules in conventions section 11.
