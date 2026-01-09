Traefik Proxy
=============

One limitation of using ports to access the container is that only a single container can be bind to a given port. Another limitation of using ports to access the container is that ports are not mnemonics. One solution to both problems is the use of a proxy.

.. mermaid::
   :align: center
   :alt: Diagram of proxy to access container.
   :caption: Diagram of proxy to access container.
   
    flowchart 
        subgraph pod0[Pod]
        proxy
        end

        subgraph pod1[Pod]
        nginx1
        end

        subgraph pod2[Pod]
        nginx2
        end

        subgraph network[Network]
        pod0
        pod1
        pod2
        end

        subgraph host[Host]
        browser
        network
        pod0
        pod1
        pod2
        end

        browser[Web browser] -->|*.localhost| proxy[Proxy];
        proxy -->|foo.localhost| nginx1[Django];
        proxy -->|bar.localhost| nginx2[Flask];

        classDef classPod fill:lightblue,stroke:blue
        class pod0 classPod;
        class pod1 classPod;
        class pod2 classPod;

        classDef classNetwork stroke:black,stroke-dasharray: 5 5
        class network classNetwork;

A popular proxy is `Traefik <https://doc.traefik.io/traefik/>`_ and it will be cover in this section.

..  note::

    The content of this section is inspired by "`Running the Traefik, my favorite Edge Router with Podman <https://willsena.dev/running-the-traefik-my-favorite-cloud-edge-router-with-podman/>`_" from William Sena.

Requirements
------------

Traefik requires access to `Podman's systemd socket <https://docs.podman.io/en/latest/markdown/podman-system-service.1.html>`_ to work. To start the socket, run

..  code:: bash

    systemctl --user start podman.socket

If you prefer, to start immediately on boot, run

..  code:: bash

    systemctl --user enable podman.socket

Usage
-----

Traefik uses labels in the pod to declare the rules for when and how traffic should be directed to the specific pod.

HTTP
^^^^

Labels used for HTTP are

- ``traefik.enable`` with the value ``true``
- ``traefik.http.routers.<router_name>.tls`` with the value ``false``
- ``traefik.http.routers.<router_name>.entrypoints`` with the value ``web``
- `traefik.http.routers.<router_name>.rule <https://doc.traefik.io/traefik/reference/routing-configuration/http/routing/rules-and-priority/#rules>`_ with matching rules, e.g. ``Host(`example.localhost`)``
- ``traefik.http.services.<service_name>.loadbalancer.server.port`` with the port used by the container, e.g. ``80``.

HTTPS
^^^^^

Traefik has built-in support for `Let's Encrypt <https://letsencrypt.org/>`_ and the reader **must** read the section "`TLS Certificate Management (Let's Encrypt) <https://doc.traefik.io/traefik/setup/docker/#tls-certificate-management-lets-encrypt>`_" from the Traekik documentation.

Labels used for HTTP are

- ``traefik.enable`` with the value ``true``
- ``traefik.http.routers.<router_name>.tls`` with the value ``true``
- ``traefik.http.routers.<router_name>.entrypoints`` with the value ``websecure``
- `traefik.http.routers.<router_name>.rule <https://doc.traefik.io/traefik/reference/routing-configuration/http/routing/rules-and-priority/#rules>`_ with matching rules, e.g. ``Host(`example.localhost`)``
- ``traefik.http.services.<service_name>.loadbalancer.server.port`` with the port used by the container, e.g. ``80``.

Example
-------

Given the following Kubernetes manifest file

.. literalinclude:: examples/nginx1/play.yml
   :language: yaml
   :caption: play.yml

running

.. code:: bash

    podman kube play play.yml

creates

- a pod named ``traefik`` with a container named ``traefik`` running the image ``docker.io/library/traefik:v3.6.6`` and the ports 80 and 8080 in the host are mapped to the port 80 and 8080, respectively, in the container.
- a pod named ``nginx-traefik`` with a container named ``nginx-traefik`` running the image ``docker.io/library/nginx:alpine``.

The Traefik dashboard can be tested with

..  code:: bash

    curl http://traefik.localhost

and the NGINX server can be tested with

..  code:: bash

    curl http://example.localhost
