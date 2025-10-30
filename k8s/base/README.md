# Kubernetes

## Someplace Knowledge

| Prefix | Ý nghĩa / Loại tài nguyên                              | Ví dụ                                         |
| ------ | ------------------------------------------------------ | --------------------------------------------- |
| 00-    | Resource nền tảng, Namespace, CRD, RBAC, NetworkPolicy | 00-ns-thudt32.yaml, 00-rbac.yaml              |
| 10-    | ConfigMap, Secret, ServiceAccount, Env Config          | 10-frontier-cm.yaml, 10-frontier-secret.yaml  |
| 20-    | PersistentVolume, PVC, StorageClass                    | 20-data-pvc.yaml                              |
| 30-    | Deployment, StatefulSet, DaemonSet                     | 30-frontier-deploy.yaml, 30-redis-deploy.yaml |
| 40-    | Service, Headless Service                              | 40-frontier-svc.yaml                          |
| 50-    | Ingress, Gateway, VirtualService                       | 50-frontier-ing.yaml                          |
| 60-    | HPA, autoscaling, CronJob, Job                         | 60-frontier-hpa.yaml                          |
| 70+    | Monitoring, NetworkPolicy, IstioPolicy, CiliumPolicy   | 70-frontier-egress.yaml, 80-alert-rule.yaml   |
