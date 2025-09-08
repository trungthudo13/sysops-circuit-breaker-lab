#!/usr/bin/env bash

kubectl apply -f docker/k8s/manifests.yaml
kubectl apply -f docker/k8s/ingress.yaml
kubectl apply -f docker/k8s/circuit-breaker.yaml
# kubectl apply -f docker/k8s/circuit-breaker-diff-path.yaml
kubectl apply -f docker/k8s/external-manifest.yaml
kubectl apply -f docker/k8s/google-external-manifest.yaml
kubectl apply -f docker/k8s/envoyfilter-fallback-outbound.yaml

kind load docker-image circuit-breaker:latest --name circuit-breaker