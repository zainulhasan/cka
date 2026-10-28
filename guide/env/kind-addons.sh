#!/usr/bin/env bash
# usage: kind-addons.sh metrics-server|gateway-api-crds|traefik|metallb|helm|kustomize
# helm and kustomize are downloaded into $BIN_DIR (default ~/.local/bin); add it to PATH.
set -euo pipefail

BIN_DIR=${BIN_DIR:-$HOME/.local/bin}
os=$(uname -s | tr '[:upper:]' '[:lower:]')
arch=$(uname -m)
case "$arch" in x86_64) arch=amd64 ;; aarch64|arm64) arch=arm64 ;; esac

# fetch_bin <tar.gz url> <binary name>: unpack the archive and copy that one binary into $BIN_DIR
fetch_bin() {
  local tmp; tmp=$(mktemp -d)
  curl -fsSL "$1" | tar -xz -C "$tmp"
  mkdir -p "$BIN_DIR"
  install -m 0755 "$(find "$tmp" -type f -name "$2" | head -1)" "$BIN_DIR/$2"
  rm -rf "$tmp"
  echo "installed $BIN_DIR/$2"
}

case "${1:?add-on name}" in
  metrics-server)
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.9.0/components.yaml
    kubectl -n kube-system patch deploy metrics-server --type=json \
      -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]' ;;
  gateway-api-crds)
    kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.6.3/standard-install.yaml ;;
  traefik)
    helm repo add traefik https://traefik.github.io/charts && helm repo update
    helm upgrade --install traefik traefik/traefik -n traefik --create-namespace --version 42.1.3 \
      --set providers.kubernetesGateway.enabled=true ;;
  metallb)
    helm repo add metallb https://metallb.github.io/metallb && helm repo update
    helm upgrade --install metallb metallb/metallb -n metallb-system --create-namespace --version 0.16.1 ;;
  helm)
    fetch_bin "https://get.helm.sh/helm-v4.3.1-$os-$arch.tar.gz" helm ;;
  kustomize)
    fetch_bin "https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv5.8.3/kustomize_v5.8.3_${os}_${arch}.tar.gz" kustomize ;;
  *) echo "unknown add-on: $1" >&2; exit 1 ;;
esac
