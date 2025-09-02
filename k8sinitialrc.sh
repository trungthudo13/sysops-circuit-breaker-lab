kind load docker-image circuit-breaker:latest --name circuit-breaker

# 1) kind
kind create cluster --name circuit-breaker --config configs/kind-config.yaml

# 2) istio
istioctl install --set profile=demo -y
kubectl create ns circuit-breaker
kubectl label ns circuit-breaker istio-injection=enabled

# 3) app
kubectl apply -f docker/k8s/manifests.yaml

# 4) ingress
kubectl apply -f docker/k8s/ingress.yaml

# 5) circuit breaker
kubectl apply -f docker/k8s/circuit-breaker.yaml

# 6) test
# curl -i http://localhost:8002/