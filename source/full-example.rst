Full Exemple
============

A full example is available at https://git.gesis.org/rse/podman/demo.

Migrating from Docker
---------------------

============================= ==============================
Docker                        Podman
============================= ==============================
``Dockerfile``                ``Dockerfile``
``docker build .``            ``podman build .``
``compose.yml``               ``play.yml``
``docker compose up``         ``podman kube play play.yml``
``docker compose up --build`` ``podman kube play --build play.yml``
============================= ==============================
