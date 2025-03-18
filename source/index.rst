.. Podman Desktop Tutorial documentation master file, created by
   sphinx-quickstart on Fri Feb 28 15:27:54 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Podman Desktop Tutorial
=======================

`Podman <https://podman.io/>`_ is an open source container management tool similar to `Docker Engine <https://docs.docker.com/engine/>`_. And `Podman Desktop <https://podman-desktop.io/>`_ is open source client for Podman similar to `Docker Desktop <https://www.docker.com/products/docker-desktop/>`_.

============================== =================================== ======================================
Feature                        Podman                              Docker
============================== =================================== ======================================
License (CLI)                  Apache License 2.0                  Apache License 2.0
Cost (CLI)                     Free                                Free
License (GUI)                  Apache License 2.0                  Proprietary
Cost (GUI)                     Free                                US$9/user/month
Multi-container applications   Based on Kubernetes specification   Based on Docker Compose specification
============================== =================================== ======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   concepts
   image-build
   k8s-manifests
   k8s-ports
   k8s-volume
