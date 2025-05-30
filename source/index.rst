.. Podman Desktop Tutorial documentation master file, created by
   sphinx-quickstart on Fri Feb 28 15:27:54 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Podman Desktop Tutorial
=======================

`Podman <https://podman.io/>`_ is an open source container management tool similar to `Docker Engine <https://docs.docker.com/engine/>`_. And `Podman Desktop <https://podman-desktop.io/>`_ is an open source client for Podman similar to `Docker Desktop <https://www.docker.com/products/docker-desktop/>`_.

.. note::

    If you have experience with Docker, you might want to jump to :doc:`full-example`.

This tutorial will guide you on how to use Podman and Podman Desktop.

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
   image-pull
   image-build
   k8s-manifest
   k8s-port
   k8s-network
   k8s-volume
   k8s-secret
   k8s-development
   production-with-podman
   production-with-k3s
   full-example
   portainer
