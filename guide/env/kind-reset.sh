#!/usr/bin/env bash
# Delete every lab-* namespace to return the cluster to baseline.
kubectl get ns -o name | grep '^namespace/lab-' | xargs -r kubectl delete --wait=false
