Full Exemple
============

A full example is available at https://git.gesis.org/rse/podman/demo.

Migrating from Docker
---------------------

=========================================== =================================================== =======================================
Docker                                      Podman                                              Summary
=========================================== =================================================== =======================================
``Dockerfile``                              ``Dockerfile``                                      Image manifest.
``docker build .``                          ``podman build .``                                  Build container image.
                                            ``secret.yml``                                      Secret manifest.
                                            ``podman kube play secret.yml``                     Create Secret.
``compose.yml``                             ``play.yml``                                        Multi-container manifest.
``docker compose up``
``docker compose up --detach``              ``podman kube play play.yml``                       Create pod.
``docker compose up --build``
``docker compose up --build --detach``      ``podman kube play --build play.yml``               Build containers and create pod.
``docker compose exec -it service /bin/sh`` ``podman container exec -it pod-container /bin/sh`` Access running container interactively.
=========================================== =================================================== =======================================
