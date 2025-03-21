Full Exemple
============

A full example is available at https://git.gesis.org/rse/podman/demo.

Migrating from Docker
---------------------

============================= ===================================== ================================
Docker                        Podman                                Summary
============================= ===================================== ================================
``Dockerfile``                ``Dockerfile``                        Image manifest.
``docker build .``            ``podman build .``                    Build container image.
``compose.yml``               ``play.yml``                          Multi-container manifest.
``docker compose up``         ``podman kube play play.yml``         Create pod.
``docker compose up --build`` ``podman kube play --build play.yml`` Build containers and create pod.
                              ``podman kube play secret.yml``       Create Secret.
============================= ===================================== ================================
