# Roadmap

All 76 topics in learning order. Written lessons are links; the rest are planned.

## Part 1 - Linux for Kubernetes

| ID | Topic | Hours | Status |
|---|---|---|---|
| T1.01 | [Bash shell essentials for exam speed](part1-linux/T1.01-bash-shell-essentials-for-exam-speed.md) | 3 | written (1 review + 1 fix) |
| T1.02 | [Text processing: grep, sed, awk, cut, sort, find, xargs](part1-linux/T1.02-text-processing-grep-sed-awk-cut.md) | 3 | written (1 review + 1 fix) |
| T1.03 | [Vim and tmux for YAML editing](part1-linux/T1.03-vim-and-tmux-for-yaml-editing.md) | 2 | written (1 review + 1 fix) |
| T1.04 | [Users, groups, permissions and sudo](part1-linux/T1.04-users-groups-permissions-and-sudo.md) | 2 | written (1 review + 1 fix) |
| T1.05 | [Processes and signals](part1-linux/T1.05-processes-and-signals.md) | 2 | written (1 review + 1 fix) |
| T1.06 | [systemd and journalctl](part1-linux/T1.06-systemd-and-journalctl.md) | 3 | written (1 review + 1 fix) |
| T1.07 | [Linux networking I: interfaces, IPs, routes, bridges, veth](part1-linux/T1.07-linux-networking-i-interfaces-ips-routes.md) | 3 | written (1 review + 1 fix) |
| T1.08 | [Linux networking II: DNS, ports, sockets and test tools](part1-linux/T1.08-linux-networking-ii-dns-ports-sockets.md) | 3 | written (1 review + 1 fix) |
| T1.09 | [Packet filtering: iptables and nftables basics](part1-linux/T1.09-packet-filtering-iptables-and-nftables-basics.md) | 3 | written (1 review + 1 fix) |
| T1.10 | [Linux namespaces and cgroups v2](part1-linux/T1.10-linux-namespaces-and-cgroups-v2.md) | 3 | ready |
| T1.11 | [Containers: images, registries and runtimes (OCI, containerd, runc, crictl)](part1-linux/T1.11-containers-images-registries-and-runtimes-oci.md) | 3 | written (1 review + 1 fix) |
| T1.12 | [TLS, PKI and openssl for Kubernetes](part1-linux/T1.12-tls-pki-and-openssl-for-kubernetes.md) | 3 | written (1 review + 1 fix) |
| T1.13 | [YAML and JSON with jq, yq and JSONPath](part1-linux/T1.13-yaml-and-json-with-jq-yq.md) | 2 | ready |
| T1.14 | [SSH and remote work across nodes](part1-linux/T1.14-ssh-and-remote-work-across-nodes.md) | 1.5 | written (1 review + 1 fix) |
| T1.15 | [Packages, kernel modules, sysctl, swap and disks](part1-linux/T1.15-packages-kernel-modules-sysctl-swap-and.md) | 2 | ready |

## Part 2 - Kubernetes basics

| ID | Topic | Hours | Status |
|---|---|---|---|
| T2.01 | Kubernetes architecture and the API model | 3 | not written yet |
| T2.02 | kubectl fluency and productivity | 4 | not written yet |
| T2.03 | Pods in depth | 3 | not written yet |
| T2.04 | Labels, selectors, annotations and namespaces | 2 | not written yet |
| T2.05 | Controllers: ReplicaSets, Deployments (basics) and garbage collection | 2 | not written yet |
| T2.06 | Services and EndpointSlices fundamentals | 2 | not written yet |
| T2.07 | Declarative object management: apply, diff, patch, replace | 2 | not written yet |
| T2.08 | Events, describe and reading object status | 1.5 | not written yet |
| T2.09 | Local practice clusters: kind and minikube | 1.5 | not written yet |
| T2.10 | Exam environment, docs navigation and time strategy | 1.5 | not written yet |

## Part 3 - CKAD

| ID | Topic | Hours | Status |
|---|---|---|---|
| T3.01 | Define, build and modify container images | 3 | not written yet |
| T3.02 | Choose and use the right workload resource | 4 | not written yet |
| T3.03 | ConfigMaps | 2 | not written yet |
| T3.04 | Create & consume Secrets | 2 | not written yet |
| T3.05 | Define resource requirements | 2 | not written yet |
| T3.06 | Requests, limits and quotas: ResourceQuota and LimitRange | 2.5 | not written yet |
| T3.07 | Utilize persistent and ephemeral volumes | 3.5 | not written yet |
| T3.08 | Multi-container Pod patterns: init, sidecar, adapter, ambassador | 3 | not written yet |
| T3.09 | Implement probes and health checks | 2.5 | not written yet |
| T3.10 | Deployments and rolling updates | 2.5 | not written yet |
| T3.11 | Deployment strategies with primitives: blue/green and canary | 2 | not written yet |
| T3.12 | [Provide and troubleshoot access to applications via Services](part3-ckad/T3.12-provide-and-troubleshoot-access-to-applications.md) | 3 | written, has a known error |
| T3.13 | Use Ingress rules to expose applications | 2.5 | not written yet |
| T3.14 | Demonstrate basic understanding of NetworkPolicies | 3 | not written yet |
| T3.15 | Understand ServiceAccounts | 2 | not written yet |
| T3.16 | Understand authentication, authorization and admission control | 3 | not written yet |
| T3.17 | Understand Application Security: SecurityContexts and capabilities | 2.5 | not written yet |
| T3.18 | Discover and use resources that extend Kubernetes: CRDs and Operators | 2.5 | not written yet |
| T3.19 | Use Helm to deploy existing packages | 2.5 | not written yet |
| T3.20 | Kustomize | 2.5 | not written yet |
| T3.21 | Understand API depreciations (API deprecations and migration) | 2 | not written yet |
| T3.22 | Utilize container logs | 1.5 | not written yet |
| T3.23 | Use built-in CLI tools to monitor Kubernetes applications | 1.5 | not written yet |
| T3.24 | Debugging in Kubernetes | 3 | not written yet |

## Part 4 - CKA

| ID | Topic | Hours | Status |
|---|---|---|---|
| T4.01 | Prepare underlying infrastructure for a Kubernetes cluster | 3 | not written yet |
| T4.02 | Create and manage Kubernetes clusters using kubeadm | 4 | not written yet |
| T4.03 | Understand extension interfaces: CNI, CSI, CRI | 2.5 | not written yet |
| T4.04 | [Manage the lifecycle of Kubernetes clusters: upgrades, etcd backup/restore, certificates, node maintenance](part4-cka/T4.04-manage-the-lifecycle-of-kubernetes-clusters.md) | 5 | written, has a known error |
| T4.05 | Implement and configure a highly-available control plane | 3.5 | not written yet |
| T4.06 | Manage role based access control (RBAC) | 3 | not written yet |
| T4.07 | Use Helm and Kustomize to install cluster components | 2.5 | not written yet |
| T4.08 | Understand CRDs, install and configure operators | 2.5 | not written yet |
| T4.09 | Application deployments: rolling updates and rollbacks (admin view) | 1.5 | not written yet |
| T4.10 | Use ConfigMaps and Secrets to configure applications (admin view, incl. encryption at rest) | 2 | not written yet |
| T4.11 | Configure workload autoscaling | 2.5 | not written yet |
| T4.12 | Primitives for robust, self-healing application deployments | 2 | not written yet |
| T4.13 | Configure Pod admission and scheduling (limits, node affinity, etc.) | 4 | not written yet |
| T4.14 | Configure volume types, access modes and reclaim policies | 2 | not written yet |
| T4.15 | Manage persistent volumes and persistent volume claims | 2 | not written yet |
| T4.16 | Implement storage classes and dynamic volume provisioning | 2 | not written yet |
| T4.17 | Understand connectivity between Pods | 2.5 | not written yet |
| T4.18 | Use ClusterIP, NodePort, LoadBalancer service types and endpoints | 2.5 | not written yet |
| T4.19 | Understand and use CoreDNS | 2.5 | not written yet |
| T4.20 | Define and enforce Network Policies | 2.5 | not written yet |
| T4.21 | Know how to use Ingress controllers and Ingress resources | 2.5 | not written yet |
| T4.22 | Use the Gateway API to manage Ingress traffic | 3.5 | not written yet |
| T4.23 | Manage and evaluate container output streams | 1.5 | not written yet |
| T4.24 | Monitor cluster and application resource usage | 1.5 | not written yet |
| T4.25 | Troubleshoot cluster components | 4 | not written yet |
| T4.26 | Troubleshoot clusters and nodes | 4 | not written yet |
| T4.27 | Troubleshoot services and networking | 3.5 | not written yet |
