# PROGRESS (source of truth; resume from here)

Decisions:
- 2026-10-27: Inputs copied to guide/inputs/. `inputs/entry.sh <ID>` prints one topic entry.
- Part 2 directory is `part2-basics`. Env scripts live in guide/env/ (unverified until step 5).
- Step 1 done (00-conventions.md written).

| ID | Title | Wave | Writer | Review verdict | Fix rounds | Status | Open "To verify" items |
|---|---|---|---|---|---|---|---|
| T1.10 | Linux namespaces and cgroups v2 | 3 | a5ab984 | PASS (r1: 1 blocker, 5 major; r2: 5 major; r3: 0 major, 7 minor) | 2 | PASS | Real kind v0.33.0/v1.37.0 + Docker output captured; open: kubeadm node, Ubuntu VM and cgroup v1 node runs (section 11) |
| T3.12 | Provide and troubleshoot access to applications via Services | 9 | a2350d7 | FAIL x3 (r3: 1 blocker, 1 major) | 3 | FIXED | Round 3 fix applied by a fresh agent (headless Service port); not re-reviewed. Outputs not captured (see section 11) |
| T4.04 | Manage the lifecycle of Kubernetes clusters | 7 | a449d04 | FAIL x3 (r3: 1 major) | 3 | FIXED | Round 3 fix applied by a fresh agent (Lab C cert check); not re-reviewed. No live VM capture (see section 11) |
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
| T2.01 | Kubernetes architecture and the API model | 5 | wf | FAIL (0B/1M/10m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T2.02 | kubectl fluency and productivity | 6 | wf | FAIL (0B/1M/10m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T2.03 | Pods in depth | 7 | wf | PASS (0B/0M/9m) | 0 | PASS |  |
| T2.04 | Labels, selectors, annotations and namespaces | 7 | wf | FAIL (0B/1M/7m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T2.05 | Controllers: ReplicaSets, Deployments (basics) and garbage collection | 8 | wf | FAIL (0B/1M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T2.06 | Services and EndpointSlices fundamentals | 8 | wf | FAIL (0B/1M/8m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T2.07 | Declarative object management: apply, diff, patch, replace | 7 | wf | FAIL (0B/2M/8m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T2.08 | Events, describe and reading object status | 8 | wf | FAIL (0B/2M/5m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T2.09 | Local practice clusters: kind and minikube | 6 | wf | FAIL (0B/3M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T2.10 | Exam environment, docs navigation and time strategy | 7 | wf | PASS (0B/0M/8m) | 0 | PASS |  |
| T3.01 | Define, build and modify container images | 7 | wf | FAIL (0B/2M/10m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.03 | ConfigMaps | 8 | wf | FAIL (0B/3M/7m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.05 | Define resource requirements | 8 | wf | FAIL (0B/2M/7m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.09 | Implement probes and health checks | 8 | wf | PASS (0B/0M/11m) | 0 | PASS |  |
| T3.18 | Discover and use resources that extend Kubernetes: CRDs and Operators | 8 | wf | FAIL (0B/3M/7m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.19 | Use Helm to deploy existing packages | 8 | wf | FAIL (0B/1M/8m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.20 | Kustomize | 8 | wf | PASS (0B/0M/6m) | 0 | PASS |  |
| T3.21 | Understand API depreciations (API deprecations and migration) | 8 | wf | FAIL (0B/2M/8m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.01 | Prepare underlying infrastructure for a Kubernetes cluster | 5 | wf | FAIL (0B/3M/13m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.02 | Create and manage Kubernetes clusters using kubeadm | 6 | wf | PASS (0B/0M/8m) | 0 | PASS |  |
| T4.03 | Understand extension interfaces: CNI, CSI, CRI | 7 | wf | FAIL (0B/5M/14m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.05 | Implement and configure a highly-available control plane | 8 | wf | FAIL (0B/2M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.17 | Understand connectivity between Pods | 8 | wf | PASS (0B/0M/8m) | 0 | PASS |  |
| T3.02 | Choose and use the right workload resource | 9 | wf | PASS (0B/0M/8m) | 0 | PASS |  |
| T3.04 | Create & consume Secrets | 9 | wf | FAIL (0B/1M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.06 | Requests, limits and quotas: ResourceQuota and LimitRange | 9 | wf | FAIL (0B/1M/5m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.07 | Utilize persistent and ephemeral volumes | 10 | wf | FAIL (0B/3M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.08 | Multi-container Pod patterns: init, sidecar, adapter, ambassador | 11 | wf | FAIL (0B/3M/7m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.10 | Deployments and rolling updates | 9 | wf | PASS (0B/0M/8m) | 0 | PASS |  |
| T3.11 | Deployment strategies with primitives: blue/green and canary | 10 | wf | PASS (0B/0M/7m) | 0 | PASS |  |
| T3.13 | Use Ingress rules to expose applications | 10 | wf | PASS (0B/0M/8m) | 0 | PASS |  |
| T3.14 | Demonstrate basic understanding of NetworkPolicies | 10 | wf | PASS (0B/0M/9m) | 0 | PASS |  |
| T3.15 | Understand ServiceAccounts | 10 | wf | PASS (0B/0M/7m) | 0 | PASS |  |
| T3.16 | Understand authentication, authorization and admission control | 11 | wf | FAIL (0B/2M/5m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.23 | Use built-in CLI tools to monitor Kubernetes applications | 9 | wf | PASS (0B/0M/11m) | 0 | PASS |  |
| T4.07 | Use Helm and Kustomize to install cluster components | 9 | wf | FAIL (0B/1M/8m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.08 | Understand CRDs, install and configure operators | 10 | wf | FAIL (0B/1M/7m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.09 | Application deployments: rolling updates and rollbacks (admin view) | 10 | wf | FAIL (0B/2M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.10 | Use ConfigMaps and Secrets to configure applications (admin view, incl. encryption at rest) | 10 | wf | PASS (0B/0M/7m) | 0 | PASS |  |
| T4.11 | Configure workload autoscaling | 10 | wf | FAIL (0B/2M/4m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.12 | Primitives for robust, self-healing application deployments | 10 | wf | FAIL (0B/4M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.14 | Configure volume types, access modes and reclaim policies | 11 | wf | FAIL (0B/2M/5m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.18 | Use ClusterIP, NodePort, LoadBalancer service types and endpoints | 10 | wf | PASS (0B/0M/5m) | 0 | PASS |  |
| T4.19 | Understand and use CoreDNS | 11 | wf | FAIL (0B/1M/8m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.20 | Define and enforce Network Policies | 11 | wf | PASS (0B/0M/9m) | 0 | PASS |  |
| T4.21 | Know how to use Ingress controllers and Ingress resources | 11 | wf | PASS (0B/0M/7m) | 0 | PASS |  |
| T4.24 | Monitor cluster and application resource usage | 10 | wf | FAIL (0B/2M/9m) | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.17 | Understand Application Security: SecurityContexts and capabilities | 12 | wf | FAIL | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T3.22 | Utilize container logs | 12 | wf | PASS | 0 | PASS |  |
| T4.06 | Manage role based access control (RBAC) | 12 | wf | PASS | 0 | PASS |  |
| T4.23 | Manage and evaluate container output streams | 13 | wf | FAIL | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.27 | Troubleshoot services and networking | 12 | wf | FAIL | 1 | FIXED | reviewed once, fixed once, not re-checked |
| T4.13 | Configure Pod admission and scheduling (limits, node affinity, etc.) | 12 | wf | - | 0 | DRAFT | written, review pending |
| T4.22 | Use the Gateway API to manage Ingress traffic | 12 | wf | - | 0 | DRAFT | written, review pending |
| T4.25 | Troubleshoot cluster components | 14 | wf | - | 0 | DRAFT | written, review pending |

Decisions (cont.):
- 2026-10-27: Re-reviews write to reviews/<ID>-review-r<N>.md so fix changelogs are not overwritten.
- 2026-10-27: T3.12 marked NEEDS-HUMAN after 2 fix rounds (rule: max 2). The remaining blocker is a one-line factual fix (headless Service port); left for a human per the no-edit-by-orchestrator rule.
- 2026-10-27: T4.04 marked NEEDS-HUMAN after 2 fix rounds. Remaining major is a one-line threshold fix (12 -> 11 or parse years too).
- 2026-10-27: Pilot round done: T1.10 PASS; T3.12, T4.04 NEEDS-HUMAN. The T1.10 writer ran a real kind cluster (downloaded the kind binary), so kind-topic writers may capture real output under the lock rules in conventions section 11.
- 2026-10-27: User rule: 1 review + 1 fix per lesson (no re-review). Statuses: PASS (clean first review), FIXED (reviewed once, fixed once, not re-checked). Fix agents are fresh agents, not the original writer. Group A (T1.01-T1.15, 14 topics) done: 2 PASS, 12 FIXED.
- 2026-10-27: T3.12 and T4.04 each got a round-3 fix (the known blocker/major from their r3 reviews) from a fresh agent; status moved NEEDS-HUMAN -> FIXED, not re-reviewed.
- 2026-10-28: Group B done: 4 PASS, 13 FIXED; 6 topics (T2.03, T2.06, T3.18-T3.21) had writer failures from a network loss while the computer slept; re-run together with group C. Started caffeinate to prevent sleep.
- 2026-10-28: Group C + retries (30 topics) done: 13 PASS, 17 FIXED, 0 failures. The 6 network-failed B topics are now written.
- 2026-10-28: Local group D stopped to hand the remainder to a cloud run (see CLOUD-RUN.md). State: T3.22, T4.06 PASS; T3.17, T4.23, T4.27 FIXED; T4.13, T4.22, T4.25 DRAFT (no review yet); T3.24, T4.15, T4.16, T4.26 not written.
