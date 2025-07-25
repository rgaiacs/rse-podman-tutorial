Pod and Port
============

Normally, we want to access the program running on the container from the host.

.. mermaid::
   :align: center
   :alt: Diagram of access container.
   :caption: Diagram of access container.
   
    flowchart 
        subgraph pod[Pod]
        nginx
        end

        subgraph network[Network]
        pod
        end

        subgraph host[Host]
        browser
        network
        pod
        end

        browser[Web browser] --> nginx[NGINX];

        classDef classPod fill:lightblue,stroke:blue
        class pod classPod;

        classDef classNetwork stroke:black,stroke-dasharray: 5 5
        class network classNetwork;

.. important::

    Because Windows and macOS cannot run containers natively, the network is more complex when working on Windows and macOS.

    .. mermaid::
        :align: center
        :alt: Diagram of access container from Windows or macOS.
        :caption: Diagram of access container from Windows or macOS.
    
        flowchart
            subgraph pod[Pod]
            nginx
            end

            subgraph network[Network]
            pod
            end

            subgraph podman-machine[Podman Machine]
            network
            end

            subgraph host[Windows or macOS]
            browser
            podman-machine
            end

            browser[Web browser] --> nginx[NGINX];

            classDef classPod fill:lightblue,stroke:blue
            class pod classPod;

            classDef classNetwork fill:orange,stroke:darkorange,stroke:black,stroke-dasharray: 5 5
            class network classNetwork;

            classDef classPodmanMachine fill:orange,stroke:darkorange
            class podman-machine classPodmanMachine;

    It is easy to think that the container is hosted in a different device on the `local area network (LAN) <https://en.wikipedia.org/wiki/Local_area_network>`_.

    .. mermaid::
        :align: center
        :alt: Diagram of access container from Windows or macOS over LAN.
        :caption: Diagram of access container from Windows or macOS over LAN.
    
        flowchart LR
            subgraph pod[Pod]
            nginx
            end

            subgraph network[Network]
            pod
            end

            subgraph podman-machine[Podman Machine]
            network
            end

            subgraph host[Windows or macOS]
            browser
            end

            browser[Web browser] --> router;
            router --> nginx[NGINX];

            classDef classPod fill:lightblue,stroke:blue
            class pod classPod;

            classDef classNetwork fill:orange,stroke:darkorange,stroke:black,stroke-dasharray: 5 5
            class network classNetwork;

            classDef classPodmanMachine fill:orange,stroke:darkorange
            class podman-machine classPodmanMachine;

The container can expose some ports (for example, the port 80 to receive HTTP requests) and the exposed port can be mapped to a port in the host. This way, a request to the port in the host is passed to the container.

.. important::

    A `know shortcoming <https://github.com/containers/podman/blob/main/rootless.md>`_ of rootless is that the host's privileged ports (TCP/IP port numbers below 1024) can not be used. A workaround is to **temporarily** make a specific port (for example, port 80) not privileged using

    .. code:: bash

        sudo sysctl net.ipv4.ip_unprivileged_port_start=80

    or **permanentily** make a specific port (for example, port 80) not privileged using

    .. code:: bash

        sudo sysctl -w net.ipv4.ip_unprivileged_port_start=80

Example
-------

Given the following Kubernetes manifest file

.. literalinclude:: examples/nginx1/play.yml
   :language: yaml
   :caption: play.yml

running

.. code:: bash

    podman kube play play.yml

creates a pod named ``nginx1`` with a container named ``nginx`` running the image ``docker.io/library/nginx:alpine`` and the port 8080 in the host is mapped to the port 80 in the container.

The NGINX server can be tested width

.. code:: bash

    curl http://localhost:8080

that is expected to return ::

    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to nginx!</title>
    <style>
    html { color-scheme: light dark; }
    body { width: 35em; margin: 0 auto;
    font-family: Tahoma, Verdana, Arial, sans-serif; }
    </style>
    </head>
    <body>
    <h1>Welcome to nginx!</h1>
    <p>If you see this page, the nginx web server is successfully installed and
    working. Further configuration is required.</p>

    <p>For online documentation and support please refer to
    <a href="http://nginx.org/">nginx.org</a>.<br/>
    Commercial support is available at
    <a href="http://nginx.com/">nginx.com</a>.</p>

    <p><em>Thank you for using nginx.</em></p>
    </body>
    </html>

Windows Subsystem for Linux (WLS)
---------------------------------

.. important::

    `Windows 10 reached the end of support <https://support.microsoft.com/en-us/windows/windows-10-support-ends-on-october-14-2025-2ca8b313-1946-43d3-b55c-2b95b107f281>`_ on 14 October 14 2025.

.. important::

    The new `Mirrored mode networking <https://learn.microsoft.com/en-us/windows/wsl/networking#mirrored-mode-networking>`_ is available on Windows 11 22H2 and higher. Old versions uses a `NAT (Network Address Translation) <https://learn.microsoft.com/en-us/windows/wsl/networking#default-networking-mode-nat>`_ based architecture for networking.


WSL allows the use of the `loopback <https://en.wikipedia.org/wiki/Loopback>`_ address from Windows to access the machine running Podman, for example

.. code:: powershell

    curl.exe http://localhost:8080

or

.. code:: powershell

    curl.exe http://127.0.0.1:8080

or

.. code:: powershell

    curl.exe http://[::1]:8080

.. warning::

    ``curl.exe http://127.0.0.1:8080`` should work but it fails when tested.

It is also possible to use the IP address in the local area network (LAN) of the machine running Podman. First, discover the IP address.

.. code:: powershell

    wsl.exe hostname -I

::

    172.25.11.50

.. important::

    The IP address might change when the WSL machine restarts.

.. note::

    The IP address can be used in ``C:\Windows\System32\drivers\etc\hosts``.

And use the IP address

.. code:: powershell

    curl.exe http://172.25.11.50:8080
