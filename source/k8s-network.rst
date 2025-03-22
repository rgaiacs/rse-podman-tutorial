Pod and Network
===============

Normally, we want for one container to access the program running on another container.

.. mermaid::
   :align: center
   :alt: Diagram of network.
   :caption: Diagram of network.

    graph LR;
        browser[Web browser] --> flask[Flask];
        flask .-> postgres[PostgreSQL];

        subgraph pod[Pod]
        flask
        postgres
        end

        subgraph host[Host]
        browser
        end

The container can be reached by another container if they are part of the same pod of if they are part of the same network.

Containers in the same Pod
--------------------------

Containers in the same pod share the IP addresses, MAC addresses and port mappings. This allows the container to be reached by another container using ``localhost:port``.

Example
^^^^^^^

Given the following Kubernetes manifest file

.. literalinclude:: examples/valkey0/play.yml
   :language: yaml
   :caption: play.yml

running ::

    podman kube play play.yml

creates a pod named ``valkey0`` with a container named ``server`` running the `Valkey <https://valkey.io/>`_ server and another container named ``client`` running a small Bash script that increases a counter every 5 seconds.

Containers in the same Network
------------------------------
