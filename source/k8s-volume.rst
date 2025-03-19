Pod with Volume
===============

Containers might need access to persistent data (for example configuration files, state files, and log files) at their start or after their termination. This can be accomplished by mounting a volume to the container. Volumes can be of many types, including

- `ConfigMapVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#configmapvolumesource-v1-core>`_
- `EmptyDirVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#emptydirvolumesource-v1-core>`_
- `EphemeralVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#ephemeralvolumesource-v1-core>`_
- `HostPathVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#hostpathvolumesource-v1-core>`_
- `NFSVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#nfsvolumesource-v1-core>`_
- `PersistentVolumeClaimVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#persistentvolumeclaimvolumesource-v1-core>`_
- `SecretVolumeSource <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#secretvolumesource-v1-core>`_

Configuration Files
-------------------

This files are **read only**. ``SecretVolumeSource`` must be used for sensitive information, for example passwords. ``ConfigMapVolumeSource`` is the preferable option for non-sensitive information. ``HostPathVolumeSource`` is also an option for non-sensitive information but can cause problems due file permissions differences with host.

.. TIP::

    ``HostPathVolumeSource`` is a great option during development.

Example with HostPathVolumeSource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. WARNING::

    Podman is not able to access files in a WSL2 machine, for example ``\\wsl.localhost\Ubuntu\home\user\file``. This feature was requested in Podman's GitHub project issue `17986 <https://github.com/containers/podman/issues/17986>`_ and `21813 <https://github.com/containers/podman/issues/21813>`_.

.. ATTENTION::

    This example does **NOT** work out of the box because the host machines must have the directory to be bind to the container.

Given the following Kubernetes manifest file

.. literalinclude:: examples/nginx2/play.yml
   :language: yaml
   :caption: play.yml

running ::

    podman kube play play.yml

creates a pod named ``nginx2`` with a container named ``nginx`` running the image ``docker.io/library/nginx:alpine`` and the port 8080 in the host is mapped to the port 80 in the container.

The NGINX server can be tested with ::

    curl http://localhost:8080

that is expected to return ::

    <!DOCTYPE html>
    <html>
        <body>
            <h1>Hello!</h1>
        </body>
    </html>

Example with ConfigMapVolumeSource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. IMPORTANT::

    The ``ConfigMap`` manifest file is bundle with the ``Pod`` manifest file.

Given the following Kubernetes manifest file

.. literalinclude:: examples/nginx3/play.yml
   :language: yaml
   :caption: play.yml

running ::

    podman kube play play.yml

creates a pod named ``nginx3`` with a container named ``nginx`` running the image ``docker.io/library/nginx:alpine`` and the port 8080 in the host is mapped to the port 80 in the container.

The NGINX server can be tested with ::

    curl http://localhost:8080

that is expected to return ::

    <!DOCTYPE html>
    <html>
        <body>
            <h1>Hello!</h1>
        </body>
    </html>

State Files
-----------

This files are, generaly, write by the container. ``PersistentVolumeClaimVolumeSource`` is the preferable option here. ``HostPathVolumeSource`` is also an option can cause problems due file permissions differences with host.

Example with HostPathVolumeSource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. WARNING::

    Podman is not able to access files in a WSL2 machine, for example ``\\wsl.localhost\Ubuntu\home\user\file``. This feature was requested in Podman's GitHub project issue `17986 <https://github.com/containers/podman/issues/17986>`_ and `21813 <https://github.com/containers/podman/issues/21813>`_.

.. ATTENTION::

    This example does **NOT** work out of the box because the host machines must have the directory to be bind to the container.

Given the following Kubernetes manifest file

.. literalinclude:: examples/postgresql0/play.yml
   :language: yaml
   :caption: play.yml

running ::

    podman kube play play.yml

creates a pod named ``postgresql`` with a container named ``db`` running the image ``docker.io/library/postgres:17.4-alpine3.21`` with a volume mounted.

Example with PersistentVolumeClaimVolumeSource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given the following Kubernetes manifest file

.. literalinclude:: examples/postgresql1/play.yml
   :language: yaml
   :caption: play.yml

running ::

    podman kube play play.yml

creates a pod named ``postgresql`` with a container named ``db`` running the image ``docker.io/library/postgres:17.4-alpine3.21`` with a volume mounted.
