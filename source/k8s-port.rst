Pod and Port
============

Normally, we want to access the program running on the container from the host.

.. mermaid::
   :align: center
   :alt: Diagram of access container.
   :caption: Diagram of access container.
   
    graph LR;
        browser[Web browser] --> flask[Flask];

        subgraph pod[Pod]
        flask
        end

        subgraph host[Host]
        browser
        end

The container can expose some ports (for example, the port 80 to receive HTTP requests) and the exposed port can be mapped to a port in the host. This way, a request to the port in the host is passed to the container.

.. important::

    Because Podman run rootless, the host's privileged ports (TCP/IP port numbers below 1024) can not be used.

Example
-------

Given the following Kubernetes manifest file

.. literalinclude:: examples/nginx1/play.yml
   :language: yaml
   :caption: play.yml

running ::

    podman kube play play.yml

creates a pod named ``nginx1`` with a container named ``nginx`` running the image ``docker.io/library/nginx:alpine`` and the port 8080 in the host is mapped to the port 80 in the container.

The NGINX server can be tested with ::

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
