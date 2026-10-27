# Conventions (every lesson must follow this file)

Target: Kubernetes v1.37 (CKA and CKAD curriculum v1.37). Pins come from `inputs/00-research-summary.md` §5.

## 1. Shell setup (define at the top of every lesson that uses kubectl)

```bash
alias k=kubectl
export do="--dry-run=client -o yaml"
export now="--force --grace-period=0"
source <(kubectl completion bash); complete -o default -F __start_kubectl k
```

Use `k` everywhere. Write `k run web --image=nginx:1.27 $do > pod.yaml`.

## 2. Lab environments

Each lab states one environment: **linux-vm**, **kind** or **vms**.

### 2.1 linux-vm (Part 1, T1.04-T1.15)
One Ubuntu LTS VM (24.04 or newer), 2 vCPU, 4 GB RAM, e.g. `multipass launch --name lab --cpus 2 --memory 4G --disk 20G`. It needs real systemd and cgroup v2. Not a container.

### 2.2 kind (Parts 2-4 unless listed under vms)
kind v0.33.0, image `kindest/node:v1.37.0` pinned by digest, 1 control plane + 2 workers, cluster name `lab`, context `kind-lab`. Create it with `env/kind-up.sh`. The config is `env/kind.yaml`, copied here:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  disableDefaultCNI: true        # Calico is installed by kind-up.sh (needed for NetworkPolicy)
  podSubnet: 192.168.0.0/16
nodes:
  - role: control-plane
    image: kindest/node:v1.37.0@sha256:a1ed56cfb0e7b93589bdf97c8cd566405a265939e3620fc4f5de89adff580ae5
    extraPortMappings:
      - { containerPort: 30080, hostPort: 30080, protocol: TCP }   # NodePort lab traffic
  - role: worker
    image: kindest/node:v1.37.0@sha256:a1ed56cfb0e7b93589bdf97c8cd566405a265939e3620fc4f5de89adff580ae5
  - role: worker
    image: kindest/node:v1.37.0@sha256:a1ed56cfb0e7b93589bdf97c8cd566405a265939e3620fc4f5de89adff580ae5
```

Add-ons, installed on demand by `env/kind-addons.sh <name>` (one function per add-on; lessons call it, they do not re-explain it):

| Add-on | Pin |
|---|---|
| calico | v3.33.0 (installed by `kind-up.sh`) |
| metrics-server | v0.9.0 (+ `--kubelet-insecure-tls` on kind) |
| gateway-api-crds | v1.6.3, standard channel |
| traefik | v3.7.x (serves Ingress and Gateway API) |
| metallb | chart 0.16.1 |
| helm | v4.3.1 |
| kustomize | standalone v5.8.3 (kubectl 1.37.1 embeds v5.8.1) |

Reset between labs: `env/kind-reset.sh` deletes all `lab-*` namespaces. Full rebuild: `kind delete cluster --name lab && env/kind-up.sh`.

### 2.3 vms (CKA node topics)
Used only by T4.01-T4.05, T4.17, T4.18, T4.23, T4.25, T4.26, T4.27 and the VM parts listed in summary §5 (T4.10 encryption at rest, T4.13 static Pods and admission plugins, T4.16 provisioner install).
Three Ubuntu LTS VMs: `cp1` (2 vCPU / 4 GB), `w1`, `w2` (2 vCPU / 2-4 GB). Prepare each with `env/vm-prereqs.sh` (swap off, kernel modules, sysctl, containerd 2.x, runc, crictl, kubeadm/kubelet/kubectl from `pkgs.k8s.io/core:/stable:/v1.37/deb`). Pod CIDR `192.168.0.0/16`, CNI Calico v3.33.0, etcd 3.7.0, local-path-provisioner v0.0.37, MetalLB chart 0.16.1. The upgrade lab installs 1.36.5 and upgrades to 1.37.1.
Learners reach nodes with `ssh <node>` and `sudo -i`, like the exam (summary E7, E8).

## 3. Names and images
- Namespace per lesson: `lab-<topicid without dots, lowercase>`, e.g. `lab-t312`. Create with `k create ns lab-t312`; clean up with `k delete ns lab-t312`.
- Test images (always pinned, never `:latest`): `busybox:1.36`, `curlimages/curl`, `nginx:1.27`. For `curlimages/curl` pin a tag from the lesson's verified run, otherwise mark it in "To verify".
- Files for a lab go in `~/lab/<topicid>/`.

## 4. Cross-links
Format: `see [T3.12](../part3-ckad/T3.12-<slug>.md)`. Link only to topics in a LOWER wave or listed as a prerequisite. Slug = title in lowercase, words joined by hyphens, at most 6 words. Part directories: `part1-linux`, `part2-basics`, `part3-ckad`, `part4-cka`.

## 5. Exam facts
Copy exam facts only from summary §2 (cite the row's URL). Anything else is written `UNVERIFIED`. Never use real exam questions, dumps, or phrases like "this was on the exam". Content must be original.
Exam-allowed doc references are only kubernetes.io/docs, kubernetes.io/blog, helm.sh/docs and (CKA only) gateway-api.sigs.k8s.io. Tools in the exam hosts: kubectl, yq, curl, wget, man (summary E9). Do not rely on `jq`, `tmux` or other tools being present in exam-style tasks; say so where a lesson uses them.

## 6. Deprecated or removed items (handle the same way everywhere)
| Item | Rule |
|---|---|
| Endpoints API | Teach EndpointSlices; mention Endpoints only as deprecated |
| Service `externalIPs` | Mention as deprecated; do not use in labs |
| `gitRepo` volume | Removed/disabled; do not use |
| ingress-nginx | Retired; use Traefik for Ingress labs |
| `kubectl run -f` | Not supported; do not use |
| kube-proxy `ipvs` | Deprecated; default to iptables (nftables where the entry says so) |
| cgroup v1 | Unsupported from 1.35; all labs assume cgroup v2 |

## 7. Output and lab style
- Real output only if you actually ran it. Otherwise label the block exactly `EXPECTED OUTPUT (not captured)` and add a line to section 11 "To verify".
- Diagrams: Mermaid unless the entry says ASCII. Max heading depth is H3 inside a section.
- Break-fix labs inject the fault with a script block named `break.sh`. Verification commands must be able to fail (use `test`/`grep -q` with an exit code, or compare an exact value).
- Every lab ends with cleanup that returns the cluster to the baseline.
- Time targets in speed drills are for the exam pace (about 6 min per task on average, 2 h for 15-20 tasks, summary E2/E3).

## 8. File and front-matter
Filename `T<id>-<slug>.md` in the right `part*/` directory. The blockquote under the title is the only header metadata:
`> Competency: ... | Domain/weight: ... | Est. time: ... | Prerequisites: T.., T..`

## 9. Depth and completeness (reader must finish the lesson with the full knowledge)
The learner reads only this lesson and the lessons it links to. Write for a motivated beginner who has never seen the topic, and still reach exam depth.
- **Explain the why before the how.** Every concept: what it is, the problem it solves, how it works internally, and what breaks without it. Never just list flags.
- **Be exhaustive on the entry's checklist and complete on fields.** For every YAML field or flag that you show, say what it does, its default, and an invalid or risky value. When a subtopic has variants (modes, types, policies), give a comparison table and one runnable example each.
- **Show the reasoning on a failure.** For every common mistake: the exact error or event text, the diagnostic commands in the order you would run them, how to read the output, then the fix. Teach a repeatable troubleshooting path, not only the answer.
- **Worked example and labs are walk-throughs.** Explain what each command does and what to look for in the output. Solutions state why each step is needed, not only the commands.
- **Go beyond the entry where it helps the learner**: add a short "Under the hood" part in section 2 (what the API server, kubelet, kernel or runtime actually does), a "Related but different" note for commonly confused concepts, and extra speed-drill or review questions when the topic is large. Do not drop or shorten anything the entry requires.
- **No hand-waving.** Phrases like "and so on", "etc.", "configure as needed", "see docs" are not allowed in place of content. Link to the official page only as an addition.
- **Length:** there is no word limit. Aim for a lesson a learner could study for the estimated time in the entry (about 1,200-2,000 words per estimated hour of study, plus code). Keep sentences short and plain.
- Reviewers: treat shallow or list-only coverage of a subtopic as a **major** problem.

## 10. Rules added after the pilot round (T1.10, T3.12, T4.04)
These fixed the problems that cost the pilots 2+ fix rounds each. Check each one before you finish.

**Accuracy**
- **Trace every lab command end to end before you write it.** For each command check namespace (`-n`), object names, selectors, ports and the port actually listening. Example mistake: a headless Service does no port translation, so clients must use the Pod port, not the Service port.
- **Never state a mechanism you cannot confirm** (for example "refused means the packet reached a Pod"). If a symptom has more than one cause, say so and give the check that tells them apart.
- **Exam statements** (what will or will not be asked, which tool is on the host) must come from summary §2 with its URL. Otherwise rewrite as advice ("a LoadBalancer Service only works if the cluster has a controller") or mark UNVERIFIED.
- **Do not invent tool output.** If you do not know the exact text of a log line or error, write the part you are sure of and mark the rest as a placeholder inside the block.
- **Heading depth:** H4 and deeper are not allowed. Use bold run-in headings instead.

**Labs**
- Every speed drill block starts with a one-line setup (namespace, objects it needs) and ends with cleanup. Drills must not leave objects (Services on a fixed nodePort, Deployments) that break the worked example or the labs that follow.
- Lab order is stated once at the start of section 7 (e.g. "B, then A, then C"). Labs must leave the cluster at baseline so any order works unless you say otherwise.
- `break.sh` must not name the faults in comments. The explanation belongs only in the collapsed solution.
- Every verification must be able to FAIL and must pass on a correct fix. Compute thresholds from the real output shape (for example certificate expiry lists print `364d` for leaf certs and `9y` for CAs) and assert exact values or counts that you checked against that shape.
- When output is captured through `k run -i ... > file`, add `sleep 2` before the command and a "re-run if the first line is missing" note, because attach can lose the first bytes.
- No nested ssh (exam hosts do not support it, summary E7). Use a second terminal, or exit back to `base`, between nodes.
- Every variant in a table (Service types, policies, modes) gets one runnable example and one way to observe the effect (patch command, test command, what to look for).

**Done criteria that need a live cluster**
- This machine has no kind or multipass, so "real output captured" criteria cannot be met. That is an accepted limitation: label blocks exactly `EXPECTED OUTPUT (not captured)`, list each in section 11, and open section 11 with a "Known limitation" paragraph naming the unmet criteria and what is needed to meet them (a 3-node kind cluster or 3 VMs). Reviewers do not raise this limitation as a major on its own.
- Real output captured from Docker is allowed for plain Linux commands. Label it `REAL OUTPUT (Docker)` and never present it as a VM or kind result.

**Fix passes**
- Before returning a corrected lesson, re-check that every earlier fix and every checklist item from the entry is still present (a fix pass once dropped a row that an earlier pass had added). Then append the changelog.
- Cross-links use the exact form in §4 (`../part3-ckad/T3.09-<slug>.md`), including between files in the same directory.

## 11. Capturing real output on kind (allowed, with limits)
A pilot writer showed that real kind output can be captured from this machine (Docker is running). Do it for kind topics when you can, so the lesson has real output instead of `EXPECTED OUTPUT (not captured)`. VM-only topics (linux-vm and vms) still cannot be captured; keep their labels.
- **One cluster at a time, machine-wide.** Take the lock first: `until mkdir /tmp/kind-lab.lock 2>/dev/null; do sleep 20; done` (give up after 20 minutes and label your outputs expected instead). Release it with `rmdir /tmp/kind-lab.lock` when you have deleted your cluster. Always release it, even on failure.
- **Use your own cluster name** `k-<topicid without dots>` (for example `k-t312`), the pinned `kindest/node:v1.37.0` image and 1 control plane + 2 workers. Use `env/kind.yaml` but you may drop `extraPortMappings` unless the lesson needs port 30080. Keep the kind binary in the scratchpad or `$TMPDIR`, never in the repo.
- **Delete your cluster when done** (`kind delete cluster --name k-<id>`) and never leave containers running.
- Paste only output you actually saw. Real output is labelled by the environment it came from, for example `REAL OUTPUT (kind v0.33.0, v1.37.0)`.
- A capture that fails or times out is not a reason to invent output: label that block expected and list it in section 11.
