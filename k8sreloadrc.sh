kubectl apply -f docker/k8s/manifests.yaml
kubectl apply -f docker/k8s/ingress.yaml
kubectl apply -f docker/k8s/circuit-breaker.yaml

kind load docker-image circuit-breaker:latest --name circuit-breaker