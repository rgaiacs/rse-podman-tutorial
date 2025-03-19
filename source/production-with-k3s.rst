Production with K3S
===================

`K3S <https://k3s.io/>`_ is lightweight certified Kubernetes that include the following enhancements:

- Distributed as a single binary.
- Lightweight datastore based on sqlite3.
- Secure by default with reasonable defaults for lightweight environments.
- External dependencies have been minimized; the only requirements are a modern kernel and cgroup mounts.
- containerd / cri-dockerd container runtime (CRI)
- Flannel Container Network Interface (CNI)
- CoreDNS Cluster DNS
- Traefik Ingress controller
- ServiceLB Load-Balancer controller
- Kube-router Network Policy controller
- Local-path-provisioner Persistent Volume controller
- Spegel distributed container image registry mirror
- Host utilities (iptables, socat, etc)
