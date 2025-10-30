# INITIALS KIND

## CREATE CLUSTER

```sh
kind create cluster --name thudt32 --config k8s/overlays/kind/kind-multi.yaml
```

## INSTALL ISTIO

```sh
istioctl install --set profile=demo -y
```

## INSTALL CILIUM

```sh
cilium install \
  --version 1.16.4 \
  --set kubeProxyReplacement=true \
  --set ingressController.enabled=true \
  --set ingressController.default=true \
  --set egressGateway.enabled=true \
  --set bpf.masquerade=true \
  --set enableIPv4Masquerade=true \
  --set hubble.relay.enabled=true
```

```sh
cilium status --wait
```

## CREATE RESOURCE

```sh
kubectl kustomize k8s/overlays/kind | kubectl apply -f -
```

## LOAD IMAGES

```sh
kind load docker-image circuit-breaker:latest --name thudt32
```

If have no image, just build its:

```sh
docker build -t circuit-breaker:latest -f ./docker/Dockerfile .
```

## INSTALL NGINX INGRESS

```sh
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
kubectl -n ingress-nginx rollout status deploy/ingress-nginx-controller
```