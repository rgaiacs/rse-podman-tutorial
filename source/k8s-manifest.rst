Kubernetes Manifest File
========================

A Kubernetes manifest file is, as defined on `Glossary of Kubernetes' official documentation <https://kubernetes.io/docs/reference/glossary>`_,

    Specification of a Kubernetes API object in JSON or YAML format.

    A manifest specifies the desired state of an object that Kubernetes will maintain when you apply the manifest. For YAML format, each file can contain multiple manifests.

Podman uses Kubernetes manifest files as a way to describe pods. This Kubernetes manifests files can be used for efficient development and deployment experience.

Podman supported the following Kubernetes kinds:

- `Pod <https://kubernetes.io/docs/concepts/workloads/pods/>`_
- `Deployment <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/>`_
- `PersistentVolumeClaim <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims>`_
- `ConfigMap <https://kubernetes.io/docs/concepts/configuration/configmap/>`_
- `Secret <https://kubernetes.io/docs/concepts/configuration/secret/>`_
- `DaemonSet <https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/>`_
- `Job <https://kubernetes.io/docs/concepts/workloads/controllers/job/>`_

Workflow
--------

Given a Kubernetes manifest file that describes a pod, the pod can be created by Podman by running

.. code:: bash

    podman kube play file.yml

.. note::

    We will name the Kubernetes manifest file used by Podman as ``play.yml`` in the rest of this tutorial.

Example
^^^^^^^

Given the following Kubernetes manifest file

.. literalinclude:: examples/nginx0/play.yml
   :language: yaml
   :caption: play.yml

running

.. code:: bash

    podman kube play play.yml

creates a pod named ``nginx0`` with a container named ``nginx`` running the image ``docker.io/library/nginx:alpine``.
