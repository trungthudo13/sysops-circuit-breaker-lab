#!/usr/bin/env bash

# 1) kind
kind create cluster --name circuit-breaker --config configs/kind-config.yaml

# 2) istio
istioctl install --set profile=demo -y
kubectl create ns circuit-breaker
kubectl label ns circuit-breaker istio-injection=enabled

kubectl apply -f docker/k8s/manifests.yaml
kubectl apply -f docker/k8s/ingress.yaml
kubectl apply -f docker/k8s/circuit-breaker.yaml
kubectl apply -f docker/k8s/external-manifest.yaml
kubectl apply -f docker/k8s/envoyfilter-fallback-outbound.yaml

kind load docker-image circuit-breaker:latest --name circuit-breaker

kubectl -n istio-system patch svc istio-ingressgateway \
  -p '{"spec":{"type":"NodePort","ports":[{"name":"http2","port":80,"nodePort":30080}]}}'