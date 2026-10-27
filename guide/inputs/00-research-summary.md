# 00 — Research Summary: Linux → Kubernetes → CKAD → CKA self-study guide

- Fetch date for every source below: 2026-10-27, 03:44–04:10 UTC. I fetched each source live during this session.
- "verified from <URL>" means I read the fact on that page on the fetch date. "UNVERIFIED" means I couldn't find it on an official page, so it's left blank and not guessed.
- Raw evidence I downloaded: the curriculum PDFs from cncf/curriculum (the current ones plus old versions 1.28–1.35), their extracted text, and the LF docs pages as Markdown.

---

## 1. Official curricula

| Item | CKAD | CKA | Source |
|---|---|---|---|
| Current curriculum file | `CKAD_Curriculum_v1.37.pdf` | `CKA_Curriculum_v1.37.pdf` | https://github.com/cncf/curriculum (repo root) |
| Commit that published it | 2026-10-01 "Update CKAD to v1.37 + Add CKNE" | 2026-10-15 "Add CKA_Curriculum_v1.37.pdf and cleanup" | https://github.com/cncf/curriculum/commits/master |
| Kubernetes version of the exam | v1.37 | v1.37 | verified from https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad and https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks |
| Same version on the product page | "Software Version: Kubernetes v1.37" | "Software Version: Kubernetes v1.37" | verified from https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/ and https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/ |
| Upstream K8s latest patch | 1.37.1, released 2026-09-15 (EOL 2027-10-28) | same | verified from https://kubernetes.io/releases/ |
| Curriculum license | CC-BY 4.0+ | CC-BY 4.0+ | https://github.com/cncf/curriculum/blob/master/README.md |

How curriculum versions are numbered: the major.minor in the file name tracks the Kubernetes version (verified from the cncf/curriculum README). The README also says the patch digit is for document iterations, but the current files carry no patch digit.

Conflicts and gaps:
- The old-versions folder has no CKA or CKAD v1.36 PDF and no CKAD v1.30 PDF.
- I compared the extracted text of every version and found the competencies are byte-identical:
  - CKA: v1.32 = v1.33 = v1.34 = v1.35 = v1.37.
  - CKAD: v1.33 = v1.34 = v1.35 = v1.37.
- I found no conflicts between the PDFs and the LF CKA program-changes page.

### 1.1 CKAD v1.37: domains, weights, competencies (verbatim, including the PDF's own spelling such as "depreciations")
I read the column order from a rendered image of page 2 of the PDF, not only from the extracted text.

**Application Design and Build — 20%**
- CKAD-1.1 Define, build and modify container images
- CKAD-1.2 Choose and use the right workload resource (Deployment, DaemonSet, CronJob, etc.)
- CKAD-1.3 Understand multi-container Pod design patterns (e.g. sidecar, init and others)
- CKAD-1.4 Utilize persistent and ephemeral volumes

**Application Deployment — 20%**
- CKAD-2.1 Use Kubernetes primitives to implement common deployment strategies (e.g. blue/green or canary)
- CKAD-2.2 Understand Deployments and how to perform rolling updates
- CKAD-2.3 Use the Helm package manager to deploy existing packages
- CKAD-2.4 Kustomize

**Application Observability and Maintenance — 15%**
- CKAD-3.1 Understand API depreciations
- CKAD-3.2 Implement probes and health checks
- CKAD-3.3 Use built-in CLI tools to monitor Kubernetes applications
- CKAD-3.4 Utilize container logs
- CKAD-3.5 Debugging in Kubernetes

**Application Environment, Configuration and Security — 25%**
- CKAD-4.1 Discover and use resources that extend Kubernetes (CRD, Operators)
- CKAD-4.2 Understand authentication, authorization and admission control
- CKAD-4.3 Understand requests, limits, quotas
- CKAD-4.4 Define resource requirements
- CKAD-4.5 Understand ConfigMaps
- CKAD-4.6 Create & consume Secrets
- CKAD-4.7 Understand ServiceAccounts
- CKAD-4.8 Understand Application Security (SecurityContexts, Capabilities, etc.)

**Services and Networking — 20%**
- CKAD-5.1 Demonstrate basic understanding of NetworkPolicies
- CKAD-5.2 Provide and troubleshoot access to applications via services
- CKAD-5.3 Use Ingress rules to expose applications

CKAD total: 24 competencies. The weights sum to 100%.

### 1.2 CKA v1.37: domains, weights, competencies (verbatim)
**Storage — 10%**
- CKA-1.1 Implement storage classes and dynamic volume provisioning
- CKA-1.2 Configure volume types, access modes and reclaim policies
- CKA-1.3 Manage persistent volumes and persistent volume claims

**Troubleshooting — 30%**
- CKA-2.1 Troubleshoot clusters and nodes
- CKA-2.2 Troubleshoot cluster components
- CKA-2.3 Monitor cluster and application resource usage
- CKA-2.4 Manage and evaluate container output streams
- CKA-2.5 Troubleshoot services and networking

**Workloads and Scheduling — 15%**
- CKA-3.1 Understand application deployments and how to perform rolling update and rollbacks
- CKA-3.2 Use ConfigMaps and Secrets to configure applications
- CKA-3.3 Configure workload autoscaling
- CKA-3.4 Understand the primitives used to create robust, self-healing, application deployments
- CKA-3.5 Configure Pod admission and scheduling (limits, node affinity, etc.)

**Cluster Architecture, Installation and Configuration — 25%**
- CKA-4.1 Manage role based access control (RBAC)
- CKA-4.2 Prepare underlying infrastructure for installing a Kubernetes cluster
- CKA-4.3 Create and manage Kubernetes clusters using kubeadm
- CKA-4.4 Manage the lifecycle of Kubernetes clusters
- CKA-4.5 Implement and configure a highly-available control plane
- CKA-4.6 Use Helm and Kustomize to install cluster components
- CKA-4.7 Understand extension interfaces (CNI, CSI, CRI, etc.)
- CKA-4.8 Understand CRDs, install and configure operators

**Servicing and Networking — 20%** (the PDF spells the domain this way)
- CKA-5.1 Understand connectivity between Pods
- CKA-5.2 Define and enforce Network Policies
- CKA-5.3 Use ClusterIP, NodePort, LoadBalancer service types and endpoints
- CKA-5.4 Use the Gateway API to manage Ingress traffic
- CKA-5.5 Know how to use Ingress controllers and Ingress resources
- CKA-5.6 Understand and use CoreDNS

CKA total: 27 competencies. The weights sum to 100%.

**Official competencies, both exams: 24 + 27 = 51.** The CKA-x.y and CKAD-x.y IDs are my own labels for cross-referencing. They are not official.

---

## 2. Exam facts (environment, rules, logistics)

| # | Fact | Status |
|---|---|---|
| E1 | Online, remotely proctored, performance-based tasks solved on the command line running Linux | verified from https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad |
| E2 | "The exams consist of 15-20 performance-based tasks." | verified from https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad |
| E3 | Duration is 2 hours for both CKA and CKAD | verified from https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks and both LF product pages |
| E4 | Pass mark is 66% for CKA and 66% for CKAD | verified from https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks |
| E5 | Scored automatically; results emailed within 24 hours | verified from https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks |
| E6 | Exam environment runs Kubernetes v1.37 and is aligned to the newest minor version "within approximately 4 to 8 weeks of the K8s release date" | verified from https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks |
| E7 | Each task is done on a designated host. An infobox gives the `ssh <nodename>` command, and you exit back to host `base` after each task. Nested ssh is not supported. | verified from https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad |
| E8 | `sudo -i` gives elevated privileges on any host | verified from https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad |
| E9 | Tools on every SSH host: "kubectl with kalias and Bash autocompletion", `yq`, `curl`, `wget`, `man`. Host `base` has none of these. | verified from https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad ("kalias" is the page's wording; the exact alias name is UNVERIFIED) |
| E10 | Do not reboot host `base`. Use Ctrl+Alt+W instead of Ctrl+W. Copy/paste in the terminal is Ctrl+Shift+C / Ctrl+Shift+V. The INSERT key is prohibited. Ctrl+Alt+K locates the cursor. | verified from https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad |
| E11 | The remote desktop has a Terminal Emulator, Firefox for allowed docs, a virtual keyboard, and VSCodium (its integrated terminal is allowed; extensions are prohibited) | verified from https://docs.linuxfoundation.org/tc-docs/certification/lf-handbook2/exam-user-interface/examui-performance-based-exams.md |
| E12 | Timer alerts at 30, 15 and 5 minutes left. "Pause Exam" does not stop the timer, and lost time is not added back after a disconnect. | verified from the same ExamUI URL as E11 |
| E13 | Allowed docs: https://kubernetes.io/docs (built-in search OK, but external results may not be opened), https://kubernetes.io/blog/, https://helm.sh/docs, task-specific docs in the "Quick Reference" box, plus https://gateway-api.sigs.k8s.io for CKA only. Translated versions are allowed. Docs installed under /usr/share and distro packages are allowed. | verified from https://docs.linuxfoundation.org/tc-docs/certification/certification-resources-allowed |
| E14 | Forbidden: notes, other devices, browsing the internet with tools like Vim/Emacs, any other app or window besides the exam | verified from https://docs.linuxfoundation.org/tc-docs/certification/lf-handbook2/exam-rules-and-policies.md |
| E15 | Exam task languages: English, Simplified Chinese, Japanese | verified from https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks |
| E16 | Certification is valid for 2 years (3 years if earned before 2024-04-01). You renew by passing the exam again. | verified from https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks |
| E17 | Price: exam only $445; with THRIVE-ONE $625; with LFS258 (CKA) or LFD259 (CKAD) $645 | verified from the CKA and CKAD LF product pages (URLs in §1) |
| E18 | 12 months to schedule and take the exam; "Two exam attempts" / "One Retake" | verified from both LF product pages |
| E19 | Retake details (waiting period, whether the retake must fall inside the 12-month window) | **UNVERIFIED**: no official page I fetched spells this out. The FAQ only says "When eligible, we do offer a retake". |
| E20 | Simulator: Killer.sh, 2 attempts, 36 hours of access per attempt, 17 questions per session. Not included with CKA-SINGLE or CKAD-SINGLE registrations. | verified from https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks and both product pages |
| E21 | Number of clusters / kubeconfig contexts in the exam | **UNVERIFIED**: the official pages describe a separate SSH host per task, not a count of clusters or contexts |
| E22 | Exact OS / distro of the exam hosts | **UNVERIFIED** |
| E23 | Versions of Helm / Kustomize / CNI / Ingress or Gateway controller used in the exam | **UNVERIFIED** |
| E24 | Refund only if bought less than 3 business days ago AND not yet scheduled or taken | verified from https://docs.linuxfoundation.org/tc-docs/certification/lf-handbook2/exam-refund-policy.md |
| E25 | System needs: one active monitor (dual monitors not supported), webcam, microphone, PSI Secure Browser. You cannot take the exam inside a VM. | verified from https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad |

Lesson-writing consequence: every lab should make the learner switch hosts with `ssh` (or switch contexts with `kubectl config use-context`), use `sudo -i`, and rely only on kubectl, yq, curl, wget and man.

---

## 3. Study resources (for topic coverage and exercise ideas only; all lesson content must be original)

I took license and last-push dates from the GitHub API on 2026-10-27. "Matches v1.37?" is my judgment from the README and its stated version.

| # | Resource | License | Last update | Covers well | Missing / weak | Matches v1.37? |
|---|---|---|---|---|---|---|
| R1 | kubernetes.io docs + kubectl Quick Reference — https://kubernetes.io/docs/reference/kubectl/quick-reference/ | CC BY 4.0 (https://github.com/kubernetes/website/blob/main/LICENSE) | live (v1.37 docs) | Everything. This is the only reference allowed in the exam. | No exam-style drills | Yes |
| R2 | dgkanatsios/CKAD-exercises — https://github.com/dgkanatsios/CKAD-exercises | MIT | 2026-10-01 | Core objects, ConfigMaps/Secrets, probes, multi-container, services, Helm, CRD basics | Kustomize depth, API deprecations, Gateway API | Mostly (no version pinned; the last commit removed legacy `kubectl run`) |
| R3 | bmuschko/ckad-crash-course — https://github.com/bmuschko/ckad-crash-course | none stated | 2026-05-19 | Exam-domain-ordered exercises with solutions | — | Probably; not pinned |
| R4 | bmuschko/cka-crash-course — https://github.com/bmuschko/cka-crash-course | none stated | 2026-08-26 | CKA-domain exercises | — | Probably; not pinned |
| R5 | bmuschko/cka-study-guide (code for the O'Reilly *CKA Study Guide 2nd ed.*) — https://github.com/bmuschko/cka-study-guide | Apache-2.0 | 2025-10-15 | Chapters match the current CKA: install/upgrade, etcd, auth, Operators/CRDs, Helm+Kustomize, scaling, scheduling, storage, Services, Ingress, **Gateway API**, NetworkPolicies, troubleshooting | — | Written for K8s 1.33. Same curriculum text, but older K8s. |
| R6 | bmuschko/ckad-study-guide (code for *CKAD Study Guide 2nd ed.*) — https://github.com/bmuschko/ckad-study-guide | Apache-2.0 | 2026-07-19 | Chapter per CKAD topic, incl. API deprecations, CRDs, security contexts | — | Written for K8s 1.28: older, check every example |
| R7 | kelseyhightower/kubernetes-the-hard-way — https://github.com/kelseyhightower/kubernetes-the-hard-way | Apache-2.0 | 2025-04-10 | Manual PKI, etcd, control-plane, kubelet, and routing bring-up | kubeadm, Helm, Gateway API | No: README references v1.32 |
| R8 | mmumshad/kubernetes-the-hard-way (Vagrant variant) — https://github.com/mmumshad/kubernetes-the-hard-way | Apache-2.0 | 2025-11-17 | Same as R7 on local VMs | Same as R7 | Older than 1.37 |
| R9 | walidshaari/Kubernetes-Certified-Administrator — https://github.com/walidshaari/Kubernetes-Certified-Administrator | CC-BY-SA-4.0 | 2026-09-18 | Curated doc links per CKA competency (kubeadm, etcd, Gateway API, Helm, Kustomize, operators) | Link list, not exercises | Updated for curriculum v1.35, which has the same competency text as v1.37 |
| R10 | David-VTUK/CKA-StudyGuide — https://github.com/David-VTUK/CKA-StudyGuide | none stated | 2026-10-12 | Narrative notes per CKA domain | — | Active; not pinned |
| R11 | chadmcrowell/CKA-Exercises — https://github.com/chadmcrowell/CKA-Exercises | none stated | 2026-08-20 | Short admin drills | Mentions v1.28 / v1.31 | Partially outdated |
| R12 | kodekloudhub/certified-kubernetes-administrator-course — https://github.com/kodekloudhub/certified-kubernetes-administrator-course | none stated | 2026-09-01 | Course notes: kubeadm, etcd, networking, security | Course-dependent | Active |
| R13 | ahmetb/kubernetes-network-policy-recipes — https://github.com/ahmetb/kubernetes-network-policy-recipes | Apache-2.0 | 2025-02-07 | NetworkPolicy patterns with diagrams | Gateway / Ingress | API is stable, still valid |
| R14 | The Kubernetes Networking Guide — https://www.tkng.io/ (src https://github.com/networkop/tkng) | Apache-2.0 | 2026-03-23 | CNI, kube-proxy, DNS, Services, Ingress internals, with labs | Assumes K8s basics | Concepts are current |
| R15 | killer.sh simulator (https://killer.sh/faq) + Killercoda "Killer Shell CKA/CKAD" scenarios (https://killercoda.com/killer-shell-cka, https://killercoda.com/killer-shell-ckad) | commercial / free scenarios | live | Exam-like environment. Killer.sh is the official simulator (E20). | Killercoda pages are JavaScript-only; scenario list UNVERIFIED | Yes (official partner) |
| R16 | jamiehannaford/what-happens-when-k8s — https://github.com/jamiehannaford/what-happens-when-k8s | none stated | 2023-10-17 | End-to-end request flow from kubectl to kubelet | — | Old, but the concepts still hold |
| R17 | k8spatterns/examples — https://github.com/k8spatterns/examples | NOASSERTION | 2026-03-29 | Sidecar/init/adapter/ambassador, health probes, config patterns | Exam drills | Mostly |

**Books** (only legally free ones were downloaded; for paid ones I used only the public TOC and companion repo):

| # | Book | Access | Use |
|---|---|---|---|
| B1 | William Shotts, *The Linux Command Line*, Seventh Internet Edition, build 25.12A — https://linuxcommand.org/tlcl.php | Free PDF, CC BY-NC-ND. Downloaded (597 pp). | Part 1 coverage: shell, permissions (ch 9), processes (ch 10), vim (ch 12), networking (ch 16), regex/text (ch 19–21), scripting (ch 24–36). Coverage only, no copying (ND license). |
| B2 | TLDP *Bash Guide for Beginners* — https://tldp.org/LDP/Bash-Beginners-Guide/html/ | Free online | Part 1 shell scripting |
| B3 | Ibryam & Huß, *Kubernetes Patterns* 2nd ed. — https://k8spatterns.com/ → free PDF via https://developers.redhat.com/e-books/kubernetes-patterns-2nd-edition | Free with Red Hat registration. Not downloaded: the site returned 403 without a login. | Part 3 pattern topics (sidecar, init, adapter, health probe, declarative deployment) |
| B4 | Muschko, *CKA Study Guide* 2nd ed. (O'Reilly, K8s 1.33) | Paid. TOC taken from R5. | Topic coverage checklist |
| B5 | Muschko, *CKAD Study Guide* 2nd ed. (O'Reilly, K8s 1.28) | Paid. TOC taken from R6. | Topic coverage checklist |

Dumps check: I found no "real exam questions" or brain-dump material in R1–R17 (I grepped the READMEs for "dump" and "real exam question" and skimmed them). Rule for writers: do not use any site that advertises actual exam questions. Killer.sh is a licensed simulator, not a dump.

---

## 4. Curriculum changes (verified against the official PDFs and announcements)

### 4.1 CKA: last real change was v1.31 → v1.32, effective 2025-02-18 00:00 UTC
Source: https://training.linuxfoundation.org/certified-kubernetes-administrator-cka-program-changes/, plus a text diff of `old-versions/CKA_Curriculum_v1.31.pdf` against `CKA_Curriculum_v1.32.pdf`. Versions v1.32 → v1.37 are textually identical (verified by diff).

| Type | Item (v1.32+ wording) | Replaces (v1.31 wording) |
|---|---|---|
| NEW | Use the Gateway API to manage Ingress traffic | — |
| NEW | Use Helm and Kustomize to install cluster components | "Awareness of manifest management and common templating tools" |
| NEW | Understand CRDs, install and configure operators | — |
| NEW | Understand extension interfaces (CNI, CSI, CRI, etc.) | "Choose an appropriate container network interface plugin" |
| NEW | Configure workload autoscaling | "Know how to scale applications" |
| NEW | Configure Pod admission and scheduling (limits, node affinity, etc.) | "Understand how resource limits can affect Pod scheduling" |
| NEW | Implement storage classes and dynamic volume provisioning | "Understand storage classes, persistent volumes" |
| NEW | Define and enforce Network Policies | (not in v1.31) |
| CHANGED | Implement and configure a highly-available control plane | "Manage a highly-available Kubernetes cluster" |
| CHANGED | Create and manage Kubernetes clusters using kubeadm | "Use Kubeadm to install a basic cluster" |
| CHANGED | Manage the lifecycle of Kubernetes clusters | "Perform a version upgrade on a Kubernetes cluster using Kubeadm" AND "Implement etcd backup and restore" are no longer named explicitly. I still teach both under CKA-4.4 because cluster lifecycle covers them; that's my inference, not official wording. |
| CHANGED | Prepare underlying infrastructure for installing a Kubernetes cluster | "Provision underlying infrastructure to deploy a Kubernetes cluster" |
| CHANGED | Troubleshoot clusters and nodes / cluster components / services and networking; Monitor cluster and application resource usage; Manage and evaluate container output streams | "Evaluate cluster and node logging", "Understand how to monitor applications", "Manage container stdout & stderr logs", "Troubleshoot application failure", "Troubleshoot cluster component failure", "Troubleshoot networking" |
| REMOVED | "Understand host networking configuration on the cluster nodes", "Know how to configure applications with persistent storage", "Understand persistent volume claims primitive" (folded into CKA-1.3) | — |
| Domain rename | "Services & Networking" → "Servicing and Networking" | — |

### 4.2 CKAD: last real change was v1.29 → v1.31 (no v1.30 PDF in the repo); after that only typo fixes
Source: text diff of `old-versions/CKAD_Curriculum_v1.29.pdf`, `v1.31`, `v1.32`, `v1.33` and the current v1.37.
- NEW in v1.31: "Kustomize"; "Discover and use resources that extend Kubernetes (CRD, Operators)" (was "(CRD)"); "Understand Application (SecurityContexts, Capabilities, etc.)" (was "Understand SecurityContexts").
- CHANGED in v1.31: "Understand Jobs and CronJobs" → "Choose and use the right workload resource (…)"; "Understanding and defining resource requirements, limits and quotas" → split into "Understanding requests, limits, and quotas" + "Define resource requirements"; "Use provided tools to monitor…" → "Use built-in CLI tools to monitor…".
- v1.32: typo edits ("Development" → "Deployment", "Understand Application Security", "deprecations" → "depreciations", "Kustomize" misspelled as "Kuztomize").
- v1.33: "Kustomize" spelled correctly again. v1.33 = v1.34 = v1.35 = v1.37 (verified by diff).

### 4.3 Kubernetes release changes the lessons must reflect (verified from the release blogs)
| Version | Change relevant to the lessons | Source |
|---|---|---|
| 1.33 | Sidecar containers GA (init container with `restartPolicy: Always`); v1 Endpoints API deprecated in favour of EndpointSlices; nftables kube-proxy backend GA; in-place Pod resize beta; `.kuberc` alpha | https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/ |
| 1.34 | `.kuberc` beta and on by default; KYAML output alpha; kubelet `cgroupDriver` setting deprecated (auto-detected from CRI, GA); ordered namespace deletion GA; swap (LimitedSwap) GA; `sleep` lifecycle action GA | https://kubernetes.io/blog/2025/08/27/kubernetes-v1-34-release/ |
| 1.35 | In-place Pod resource resize **GA**; kubelet fails on cgroup v1 by default (`failCgroupV1: true`) and kubeadm init/join/upgrade check for it; kube-proxy `ipvs` mode deprecated (use nftables); last release to support containerd 1.x; Ingress NGINX retirement announced; KYAML beta | https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/ |
| 1.36 | Service `.spec.externalIPs` deprecated (removal planned for v1.43); `gitRepo` volume permanently disabled; user namespaces in Pods GA; OCI image volume source GA; MutatingAdmissionPolicy GA | https://kubernetes.io/blog/2026/04/22/kubernetes-v1-36-release/ , https://kubernetes.io/blog/2026/05/14/kubernetes-v1-36-deprecation-and-removal-of-service-externalips/ |
| 1.37 | kube-dns deprecated (CoreDNS only); ipvs timeline: off by default around v1.40, removed around v1.43; `kubectl run -f` deprecated; static Pods can no longer reference Secrets/ConfigMaps; `metrics.k8s.io` API stable; KYAML stable; HPA configurable tolerance stable; HPA scale-to-zero beta; Pod Certificates + ClusterTrustBundles stable | https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/ |
| ecosystem | **Ingress NGINX retired**: best-effort maintenance ended March 2026, and the repo is now **archived** (GitHub API `archived=true`; last release `controller-v1.15.1`, 2026-03-19). The Ingress API is GA but **frozen**, and the Kubernetes project recommends Gateway API. | https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/ , https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/ |
| ecosystem | Gateway API v1.6 (TCPRoute/UDPRoute moved to Standard); latest release v1.6.3 | https://kubernetes.io/blog/2026/08/03/gateway-api-v1-6-release/ , https://github.com/kubernetes-sigs/gateway-api/releases |
| ecosystem | Helm 4 is current (v4.3.1). minikube 1.39 ships a Helm 4 guest client. | https://github.com/helm/helm/releases , https://github.com/kubernetes/minikube/releases |

Pod Security Admission (PSA) is not named in either v1.37 curriculum. It is taught inside CKAD-4.2/4.8 and CKA-3.5 as part of admission control. That placement is my inference.

---

## 5. Practice environment plan and pinned versions

Versions are the latest GitHub release on 2026-10-27, unless noted.

| Part | Environment | Why |
|---|---|---|
| 1 Linux | One Ubuntu LTS VM (Multipass v1.17.0, or KVM on a mini PC), 2 vCPU, 4 GB RAM. Current Ubuntu LTS number: UNVERIFIED (releases.ubuntu.com did not parse); use 24.04 LTS or newer. | Needs systemd, cgroup v2, iptables/nftables, namespaces. A real VM, not a container. |
| 2 Basics | **kind v0.33.0**, node image `kindest/node:v1.37.0@sha256:a1ed56cfb0e7b93589bdf97c8cd566405a265939e3620fc4f5de89adff580ae5` (default in v0.33.0), 1 control-plane + 2 workers | Fast, disposable, multi-node. minikube v1.39.0 (default K8s v1.37.0, containerd runtime) is the alternative. |
| 3 CKAD | kind as above, plus `disableDefaultCNI: true` + Calico v3.33.0 for NetworkPolicy labs; metrics-server v0.9.0 (`--kubelet-insecure-tls` on kind, verify); Traefik v3.7.16 (one controller serving both Ingress and Gateway API) or NGINX Gateway Fabric v2.8.0 / Envoy Gateway v1.9.3 for Gateway-only labs; Gateway API CRDs v1.6.3 standard channel; Helm v4.3.1; standalone kustomize v5.8.3 (kubectl 1.37.1 embeds kustomize v5.8.1, from go.mod); Docker or Podman + BuildKit v0.34.1 for image builds | Everything CKAD needs runs on kind |
| 4 CKA | **3–4 Ubuntu VMs** (Multipass or KVM): `cp1` (2 vCPU / 4 GB), `w1`, `w2` (2 vCPU / 2–4 GB). HA variant: `cp1–cp3` + kube-vip v1.3.1 (or HAProxy+keepalived). Packages from `pkgs.k8s.io/core:/stable:/v1.37/deb` (verified on https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/); upgrade lab: install **1.36.5**, upgrade to **1.37.1**; containerd v2.4.2 (≥ 2.0 required after 1.35), runc v1.5.2, crictl v1.37.0, etcd **3.7.0** (kubeadm 1.37 `DefaultEtcdVersion = "3.7.0-0"`, from kubernetes v1.37.1 source; upstream latest is v3.7.3), Calico v3.33.0 (or Cilium v1.20.4 / Flannel v0.28.10, which has no NetworkPolicy support of its own), MetalLB (chart 0.16.1) for LoadBalancer, local-path-provisioner v0.0.37 for dynamic PVs, jq 1.8.2, yq v4.54.1 | Upgrades, etcd backup/restore, static pods, kubelet/cert/node break-fix, and HA all need real nodes with systemd |

Topics that **need kubeadm VMs**: T4.01–T4.05, T4.17, T4.18, T4.23, T4.25, T4.26. Topics with a VM-only part: T1.04–T1.15 (Linux VM), T4.10 (encryption at rest), T4.13 (static Pods/admission plugins), T4.16 (provisioner install), T4.27 (node layers). All other topics run on kind.

---

## 6. Open questions for you (max 5)
1. **Helm version**: teach Helm 4 (current, v4.3.1) with a note on Helm 3 differences? The Helm version in the exam is UNVERIFIED.
2. **Ingress controller for labs**: Ingress NGINX is retired and archived. Can I standardise on **Traefik v3.7.x** for both Ingress and Gateway API labs?
3. **Lab host**: run the Part 4 kubeadm VMs on your Mac with Multipass (needs about 10–12 GB free RAM for 3 VMs), or on the planned mini PC with KVM/Proxmox?
4. **CNI for the CKA labs**: Calico (NetworkPolicy, BGP-free default) or Cilium (eBPF, Gateway API built in)? I recommend Calico because its install is simpler for exam-style practice.
5. **Lesson size**: is about 2–4 hours of study per lesson (as estimated in the backlog) the right granularity, or do you want smaller lessons?

## 7. UNVERIFIED items in this file
E9 alias name, E19 retake details, E21 cluster/context count, E22 exam host OS, E23 tool versions in the exam, current Ubuntu LTS number, metrics-server `--kubelet-insecure-tls` need on kind, Killercoda scenario list, Kubernetes Patterns PDF access (login wall). **Total: 9.**
