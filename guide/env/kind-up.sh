#!/usr/bin/env bash
# Create the standard 3-node kind cluster "lab" with Calico. Unverified until step 5.
set -euo pipefail
here=$(dirname "$0")
kind create cluster --name lab --config "$here/kind.yaml"
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.33.0/manifests/calico.yaml
kubectl -n kube-system rollout status ds/calico-node --timeout=180s
kubectl wait --for=condition=Ready nodes --all --timeout=180s
