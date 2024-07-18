helm upgrade cilium ./cilium \
   --namespace kube-system \
   --reuse-values \
   --set l2announcements.enabled=true \
   --set kubeProxyReplacement=true \
   --set k8sServiceHost=${API_SERVER_IP} \
   --set k8sServicePort=${API_SERVER_PORT} \
   --set k8sClientRateLimit.qps={QPS} \
   --set k8sClientRateLimit.burst={BURST} \
   --set l2announcements.leaseDuration=3s \
   --set l2announcements.leaseRenewDeadline=1s \
   --set l2announcements.leaseRetryPeriod=200ms

helm upgrade cilium ./cilium \
   --namespace kube-system \
   --reuse-values \
   --set l2podAnnouncements.enabled=true \
   --set l2podAnnouncements.interface=ens18