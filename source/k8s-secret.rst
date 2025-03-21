Pod with Sensitive Information
==============================

Sensitive information, for example passwords, should be managed with special care. Volumes that store sensitive information are called Secret and are similar to ConfigMap.

Workflow
--------

New Secret can be created by running ::

    podman kube play secret.yml

where ``secret.yml`` is a Kubernetes manifest file like ::

    apiVersion: v1
    kind: Secret
    metadata:
        name: password
    stringData:
        password: 123456

.. danger::

    Sensitive information must **ALWAYS** be encrypted when stored in a file. In other words, **NEVER** store your ``secret.yml``.

.. danger::

    Sensitive information must **NEVER** be stored in your shell history. **ALWAYS** prepend the command with a white space to avoid the command to be recorded on the shell history.

After creation, Secret can be referenced by another Kubernetes manifest file like ::

    apiVersion: v1
    kind: Pod
    metadata:
        ...
    spec:
        containers:
            - volumeMounts:
                - mountPath: /path/to/dir
                  name: password-volume
        volumes:
            - secret:
                secretName: password
              name: password-volume

Each key in ``stringData`` will be one file in ``mountPath``.

Example
^^^^^^^

Given the following Kubernetes manifest file

.. literalinclude:: examples/nginx-secret0/secret.yml
   :language: yaml
   :caption: secret.yml

running ::

    podman kube play secret.yml

creates a Secret named ``html``.

Given the following Kubernetes manifest file

.. literalinclude:: examples/nginx-secret0/play.yml
   :language: yaml
   :caption: play.yml

running ::

    podman kube play play.yml

creates a pod named ``nginx-secret0`` with

- a container named ``nginx`` running the image ``docker.io/library/nginx:alpine``,
- the port 8080 in the host is mapped to the port 80 in the container,
- the Secret ``html`` mounted in ``/usr/share/nginx/html``.

The NGINX server can be tested with ::

    curl http://localhost:8080

that is expected to return ::

    <!DOCTYPE html>
    <html>
        <body>
            <p>This is a secret.</p>
        </body>
    </html>
