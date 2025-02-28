Concepts
========

Pod
---

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

Example
^^^^^^^

::

    $ podman pod create tutorial
    $ podman pod start tutorial
    $ podman create \
        --pod tutorial \
        --name hello \
        quay.io/podman/hello:latest
    $ podman start \
        --attach \
        hello

outputs ::

    !... Hello Podman World ...!

            .--"--.           
        / -     - \         
        / (O)   (O) \        
    ~~~| -=(,Y,)=- |         
        .---. /`  \   |~~      
    ~/  o  o \~~~~.----. ~~   
    | =(X)= |~  / (O (O) \   
    ~~~~~~~  ~| =(Y_)=-  |   
    ~~~~    ~~~|   U      |~~ 

    Project:   https://github.com/containers/podman
    Website:   https://podman.io
    Desktop:   https://podman-desktop.io
    Documents: https://docs.podman.io
    YouTube:   https://youtube.com/@Podman
    X/Twitter: @Podman_io
    Mastodon:  @Podman_io@fosstodon.org
