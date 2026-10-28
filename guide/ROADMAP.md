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
| T2.01 | [Kubernetes architecture and the API model](part2-basics/T2.01-kubernetes-architecture-and-the-api-model.md) | 3 | written (1 review + 1 fix) |
| T2.02 | [kubectl fluency and productivity](part2-basics/T2.02-kubectl-fluency-and-productivity.md) | 4 | written (1 review + 1 fix) |
| T2.03 | [Pods in depth](part2-basics/T2.03-pods-in-depth.md) | 3 | ready |
| T2.04 | [Labels, selectors, annotations and namespaces](part2-basics/T2.04-labels-selectors-annotations-and-namespaces.md) | 2 | written (1 review + 1 fix) |
| T2.05 | [Controllers: ReplicaSets, Deployments (basics) and garbage collection](part2-basics/T2.05-controllers-replicasets-deployments-basics-and-garbage.md) | 2 | written (1 review + 1 fix) |
| T2.06 | [Services and EndpointSlices fundamentals](part2-basics/T2.06-services-and-endpointslices-fundamentals.md) | 2 | written (1 review + 1 fix) |
| T2.07 | [Declarative object management: apply, diff, patch, replace](part2-basics/T2.07-declarative-object-management-apply-diff-patch.md) | 2 | written (1 review + 1 fix) |
| T2.08 | [Events, describe and reading object status](part2-basics/T2.08-events-describe-and-reading-object-status.md) | 1.5 | written (1 review + 1 fix) |
| T2.09 | [Local practice clusters: kind and minikube](part2-basics/T2.09-local-practice-clusters-kind-and-minikube.md) | 1.5 | written (1 review + 1 fix) |
| T2.10 | [Exam environment, docs navigation and time strategy](part2-basics/T2.10-exam-environment-docs-navigation-and-time.md) | 1.5 | ready |

## Part 3 - CKAD

| ID | Topic | Hours | Status |
|---|---|---|---|
| T3.01 | [Define, build and modify container images](part3-ckad/T3.01-define-build-and-modify-container-images.md) | 3 | written (1 review + 1 fix) |
| T3.02 | [Choose and use the right workload resource](part3-ckad/T3.02-choose-and-use-the-right-workload.md) | 4 | ready |
| T3.03 | [ConfigMaps](part3-ckad/T3.03-configmaps.md) | 2 | written (1 review + 1 fix) |
| T3.04 | [Create & consume Secrets](part3-ckad/T3.04-create-consume-secrets.md) | 2 | written (1 review + 1 fix) |
| T3.05 | [Define resource requirements](part3-ckad/T3.05-define-resource-requirements.md) | 2 | written (1 review + 1 fix) |
| T3.06 | [Requests, limits and quotas: ResourceQuota and LimitRange](part3-ckad/T3.06-requests-limits-and-quotas-resourcequota-and.md) | 2.5 | written (1 review + 1 fix) |
| T3.07 | [Utilize persistent and ephemeral volumes](part3-ckad/T3.07-utilize-persistent-and-ephemeral-volumes.md) | 3.5 | written (1 review + 1 fix) |
| T3.08 | [Multi-container Pod patterns: init, sidecar, adapter, ambassador](part3-ckad/T3.08-multi-container-pod-patterns-init-sidecar.md) | 3 | written (1 review + 1 fix) |
| T3.09 | [Implement probes and health checks](part3-ckad/T3.09-implement-probes-and-health-checks.md) | 2.5 | ready |
| T3.10 | [Deployments and rolling updates](part3-ckad/T3.10-deployments-and-rolling-updates.md) | 2.5 | ready |
| T3.11 | [Deployment strategies with primitives: blue/green and canary](part3-ckad/T3.11-deployment-strategies-with-primitives-blue-green.md) | 2 | ready |
| T3.12 | [Provide and troubleshoot access to applications via Services](part3-ckad/T3.12-provide-and-troubleshoot-access-to-applications.md) | 3 | written (1 review + 1 fix) |
| T3.13 | [Use Ingress rules to expose applications](part3-ckad/T3.13-use-ingress-rules-to-expose-applications.md) | 2.5 | ready |
| T3.14 | [Demonstrate basic understanding of NetworkPolicies](part3-ckad/T3.14-demonstrate-basic-understanding-of-networkpolicies.md) | 3 | ready |
| T3.15 | [Understand ServiceAccounts](part3-ckad/T3.15-understand-serviceaccounts.md) | 2 | ready |
| T3.16 | [Understand authentication, authorization and admission control](part3-ckad/T3.16-understand-authentication-authorization-and-admission-control.md) | 3 | written (1 review + 1 fix) |
| T3.17 | [Understand Application Security: SecurityContexts and capabilities](part3-ckad/T3.17-understand-application-security-securitycontexts-and-capabilities.md) | 2.5 | written (1 review + 1 fix) |
| T3.18 | [Discover and use resources that extend Kubernetes: CRDs and Operators](part3-ckad/T3.18-discover-and-use-resources-that-extend.md) | 2.5 | written (1 review + 1 fix) |
| T3.19 | [Use Helm to deploy existing packages](part3-ckad/T3.19-use-helm-to-deploy-existing-packages.md) | 2.5 | written (1 review + 1 fix) |
| T3.20 | [Kustomize](part3-ckad/T3.20-kustomize.md) | 2.5 | ready |
| T3.21 | [Understand API depreciations (API deprecations and migration)](part3-ckad/T3.21-understand-api-depreciations-api-deprecations-and.md) | 2 | written (1 review + 1 fix) |
| T3.22 | [Utilize container logs](part3-ckad/T3.22-utilize-container-logs.md) | 1.5 | ready |
| T3.23 | [Use built-in CLI tools to monitor Kubernetes applications](part3-ckad/T3.23-use-built-in-cli-tools-to.md) | 1.5 | ready |
| T3.24 | Debugging in Kubernetes | 3 | not written yet |

## Part 4 - CKA

| ID | Topic | Hours | Status |
|---|---|---|---|
| T4.01 | [Prepare underlying infrastructure for a Kubernetes cluster](part4-cka/T4.01-prepare-underlying-infrastructure-for-a-kubernetes.md) | 3 | written (1 review + 1 fix) |
| T4.02 | [Create and manage Kubernetes clusters using kubeadm](part4-cka/T4.02-create-and-manage-kubernetes-clusters-using.md) | 4 | ready |
| T4.03 | [Understand extension interfaces: CNI, CSI, CRI](part4-cka/T4.03-understand-extension-interfaces-cni-csi-cri.md) | 2.5 | written (1 review + 1 fix) |
| T4.04 | [Manage the lifecycle of Kubernetes clusters: upgrades, etcd backup/restore, certificates, node maintenance](part4-cka/T4.04-manage-the-lifecycle-of-kubernetes-clusters.md) | 5 | written (1 review + 1 fix) |
| T4.05 | [Implement and configure a highly-available control plane](part4-cka/T4.05-implement-and-configure-a-highly-available.md) | 3.5 | written (1 review + 1 fix) |
| T4.06 | [Manage role based access control (RBAC)](part4-cka/T4.06-manage-role-based-access-control-rbac.md) | 3 | ready |
| T4.07 | [Use Helm and Kustomize to install cluster components](part4-cka/T4.07-use-helm-and-kustomize-to-install.md) | 2.5 | written (1 review + 1 fix) |
| T4.08 | [Understand CRDs, install and configure operators](part4-cka/T4.08-understand-crds-install-and-configure-operators.md) | 2.5 | written (1 review + 1 fix) |
| T4.09 | [Application deployments: rolling updates and rollbacks (admin view)](part4-cka/T4.09-application-deployments-rolling-updates-and-rollbacks.md) | 1.5 | written (1 review + 1 fix) |
| T4.10 | [Use ConfigMaps and Secrets to configure applications (admin view, incl. encryption at rest)](part4-cka/T4.10-use-configmaps-and-secrets-to-configure.md) | 2 | ready |
| T4.11 | [Configure workload autoscaling](part4-cka/T4.11-configure-workload-autoscaling.md) | 2.5 | written (1 review + 1 fix) |
| T4.12 | [Primitives for robust, self-healing application deployments](part4-cka/T4.12-primitives-for-robust-self-healing-application.md) | 2 | written (1 review + 1 fix) |
| T4.13 | [Configure Pod admission and scheduling (limits, node affinity, etc.)](part4-cka/T4.13-configure-pod-admission-and-scheduling-limits.md) | 4 | written |
| T4.14 | [Configure volume types, access modes and reclaim policies](part4-cka/T4.14-configure-volume-types-access-modes-and.md) | 2 | written (1 review + 1 fix) |
| T4.15 | Manage persistent volumes and persistent volume claims | 2 | not written yet |
| T4.16 | Implement storage classes and dynamic volume provisioning | 2 | not written yet |
| T4.17 | [Understand connectivity between Pods](part4-cka/T4.17-understand-connectivity-between-pods.md) | 2.5 | ready |
| T4.18 | [Use ClusterIP, NodePort, LoadBalancer service types and endpoints](part4-cka/T4.18-use-clusterip-nodeport-loadbalancer-service-types.md) | 2.5 | ready |
| T4.19 | [Understand and use CoreDNS](part4-cka/T4.19-understand-and-use-coredns.md) | 2.5 | written (1 review + 1 fix) |
| T4.20 | [Define and enforce Network Policies](part4-cka/T4.20-define-and-enforce-network-policies.md) | 2.5 | ready |
| T4.21 | [Know how to use Ingress controllers and Ingress resources](part4-cka/T4.21-know-how-to-use-ingress-controllers.md) | 2.5 | ready |
| T4.22 | [Use the Gateway API to manage Ingress traffic](part4-cka/T4.22-use-the-gateway-api-to-manage.md) | 3.5 | written |
| T4.23 | [Manage and evaluate container output streams](part4-cka/T4.23-manage-and-evaluate-container-output-streams.md) | 1.5 | written (1 review + 1 fix) |
| T4.24 | [Monitor cluster and application resource usage](part4-cka/T4.24-monitor-cluster-and-application-resource-usage.md) | 1.5 | written (1 review + 1 fix) |
| T4.25 | [Troubleshoot cluster components](part4-cka/T4.25-troubleshoot-cluster-components.md) | 4 | written |
| T4.26 | Troubleshoot clusters and nodes | 4 | not written yet |
| T4.27 | [Troubleshoot services and networking](part4-cka/T4.27-troubleshoot-services-and-networking.md) | 3.5 | written (1 review + 1 fix) |
