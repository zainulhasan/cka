#!/usr/bin/env bash
# usage: kind-addons.sh metrics-server|gateway-api-crds|traefik|metallb|helm  (URLs/flags unverified until step 5)
set -euo pipefail
case "${1:?add-on name}" in
  metrics-server)
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.9.0/components.yaml
    kubectl -n kube-system patch deploy metrics-server --type=json \
      -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]' ;;
  gateway-api-crds)
    kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.6.3/standard-install.yaml ;;
  traefik)
    helm repo add traefik https://traefik.github.io/charts && helm repo update
    helm upgrade --install traefik traefik/traefik -n traefik --create-namespace \
      --set providers.kubernetesGateway.enabled=true ;;
  metallb)
    helm repo add metallb https://metallb.github.io/metallb && helm repo update
    helm upgrade --install metallb metallb/metallb -n metallb-system --create-namespace --version 0.16.1 ;;
  *) echo "unknown add-on: $1" >&2; exit 1 ;;
esac
