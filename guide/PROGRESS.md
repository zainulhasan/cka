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
| T1.01 | Bash shell essentials for exam speed | 1 | wf | FAIL (0B/2M/8m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.02 | Text processing: grep, sed, awk, cut, sort, find, xargs | 2 | wf | FAIL (0B/2M/6m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.03 | Vim and tmux for YAML editing | 2 | wf | FAIL (0B/1M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.04 | Users, groups, permissions and sudo | 2 | wf | FAIL (0B/3M/8m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.05 | Processes and signals | 2 | wf | FAIL (0B/1M/10m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.06 | systemd and journalctl | 3 | wf | FAIL (1B/4M/12m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.07 | Linux networking I: interfaces, IPs, routes, bridges, veth | 2 | wf | FAIL (0B/2M/10m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.08 | Linux networking II: DNS, ports, sockets and test tools | 3 | wf | FAIL (0B/1M/12m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.09 | Packet filtering: iptables and nftables basics | 3 | wf | FAIL (0B/2M/7m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.11 | Containers: images, registries and runtimes (OCI, containerd, runc, crictl) | 4 | wf | FAIL (0B/2M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.12 | TLS, PKI and openssl for Kubernetes | 3 | wf | FAIL (0B/3M/8m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.13 | YAML and JSON with jq, yq and JSONPath | 2 | wf | PASS (0B/0M/9m) | 0 | PASS |  |
| T1.14 | SSH and remote work across nodes | 3 | wf | FAIL (0B/1M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T1.15 | Packages, kernel modules, sysctl, swap and disks | 4 | wf | PASS (0B/0M/13m) | 0 | PASS |  |

Decisions (cont.):
- 2026-10-27: Re-reviews write to reviews/<ID>-review-r<N>.md so fix changelogs are not overwritten.
- 2026-10-27: T3.12 marked NEEDS-HUMAN after 2 fix rounds (rule: max 2). The remaining blocker is a one-line factual fix (headless Service port); left for a human per the no-edit-by-orchestrator rule.
- 2026-10-27: T4.04 marked NEEDS-HUMAN after 2 fix rounds. Remaining major is a one-line threshold fix (12 -> 11 or parse years too).
- 2026-10-27: Pilot round done: T1.10 PASS; T3.12, T4.04 NEEDS-HUMAN. The T1.10 writer ran a real kind cluster (downloaded the kind binary), so kind-topic writers may capture real output under the lock rules in conventions section 11.
- 2026-10-27: User rule: 1 review + 1 fix per lesson (no re-review). Statuses: PASS (clean first review), FIXED (reviewed once, fixed once, not re-checked). Fix agents are fresh agents, not the original writer. Group A (T1.01-T1.15, 14 topics) done: 2 PASS, 12 FIXED.
