Pod and Network
===============

Normally, we want for one container to access the program running on another container. Two scenarios are possible: containers run on the same pod or containers run on different pods.

Containers on the same Pod
--------------------------

.. mermaid::
    :align: center
    :alt: Diagram of containers running on the same pod.
    :caption: Diagram of containers running on the same pod.

    flowchart 
        subgraph pod[Pod]
        flask
        postgres
        end

        subgraph network[Network]
        pod
        end

        subgraph host[Host]
        browser
        network
        pod
        end

        browser[Web browser] --> flask[Flask];
        flask .-> postgres[PostgreSQL];

        classDef classPod fill:lightblue,stroke:blue
        class pod classPod;

        classDef classNetwork stroke:black,stroke-dasharray: 5 5
        class network classNetwork;

Containers in the same pod share the IP addresses, MAC addresses and port mappings. This allows the container to be reached by another container using ``localhost`` or the name of the container.

Example
^^^^^^^

Given the following Kubernetes manifest file

.. literalinclude:: examples/valkey0/play.yml
   :language: yaml
   :caption: play.yml

running ::

    podman kube play play.yml

creates a pod named ``valkey0`` with a container named ``server`` running the `Valkey <https://valkey.io/>`_ server and another container named ``client`` running a small Bash script that increases a counter every 5 seconds.

Containers on different pods
----------------------------

.. mermaid::
    :align: center
    :alt: Diagram of containers running on different pods.
    :caption: Diagram of containers running on different pods.

    flowchart 
        subgraph pod1[Pod 1]
        flask
        end

        subgraph pod2[Pod 2]
        postgres
        end

        subgraph network[Network]
        pod1
        pod2
        end

        subgraph host[Host]
        browser
        network
        pod1
        pod2
        end

        browser[Web browser] --> flask[Flask];
        flask .-> postgres[PostgreSQL];

        classDef classPod fill:lightblue,stroke:blue
        class pod1,pod2 classPod;

        classDef classNetwork stroke:black,stroke-dasharray: 5 5
        class network classNetwork;

The container can be reached by another container if they are part of the same pod of if they are part of the same network.

Example
^^^^^^^

.. important::

    When no network option is specified and host network mode is not configured in the YAML file, a new network stack is created and pods are attached to it making possible pod to pod communication.

First, create a new network by running ::

    podman network valkey1

Given the following Kubernetes manifest file

.. literalinclude:: examples/valkey1/play.yml
   :language: yaml
   :caption: play.yml

running ::

    podman kube play --net valkey1 play.yml

creates a pod named ``valkey1-server`` connected to the network ``valkey1`` with a container named ``server`` running the `Valkey <https://valkey.io/>`_ server and another pod named ``valkey1-client`` connected to the network ``valkey1`` with a container named ``client`` running a small Bash script that increases a counter every 5 seconds.
