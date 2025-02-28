Pod
===

A pod is defined in the `Kubernetes documentation <https://kubernetes.io/docs/concepts/workloads/pods/>`_ as

> A Pod (as in a pod of whales or pea pod) is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers.

Create a pod by running ::

    podman pod create pod-name

Start the pod by running ::

    podman pod start pod-name

Add a container to the pod by running ::

    podman create \
    --pod pod-name \
    --name container-name \
    image

Start the container by running ::

    podman start \
    container-name
