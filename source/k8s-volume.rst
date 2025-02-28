Pod with Volume
===============

Containers might need access to some user files or might need to persist data after their termination. This can be accomplished by mounting a volume to the container. Volumes can be of many types but the more relevants are

- `ConfigMapVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#configmapvolumesource-v1-core>`_
- `EmptyDirVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#emptydirvolumesource-v1-core>`_
- `EphemeralVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#ephemeralvolumesource-v1-core>`_
- `HostPathVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#hostpathvolumesource-v1-core>`_
- `NFSVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nfsvolumesource-v1-core>`_
- `PersistentVolumeClaimVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#persistentvolumeclaimvolumesource-v1-core>`_
- `SecretVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#secretvolumesource-v1-core>`_

Load User Files
---------------

Example
^^^^^^^

Write to Persistent Files
-------------------------

Example
^^^^^^^

Given the following Kubernetes manifest file

.. literalinclude:: examples/postgresql/pod.yml
   :language: yaml

Running ::

    podman kube play examples/postgresql/pod.yml

creates a pod named ``postgresql`` with a container named ``db`` running the image ``docker.io/library/postgres:17.4-alpine3.21`` with a volume mounted.
