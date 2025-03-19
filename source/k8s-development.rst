Development with Pod
====================

During development, it is recommended that contributors

1. load dependencies from the same container image and
2. mount the source code as a volume.

The reasoning here is

1. to avoid different behaviour caused by the use of different versions of the dependencies and
2. to avoid the time costly process of create new container image.

Workflow
--------

1. Build the container image as described in :doc:`image-build`.
2. Run a pod as described in :doc:`k8s-volume`.
3. Rebuild the container image as described in :doc:`image-build`.
4. Delete and recreate the pod as described in :doc:`k8s-volume`.

Example
-------

.. imporant::

    The commands are run from the root of the project.

Given the following ``Dockerfile``

.. literalinclude:: examples/flask0/Dockerfile
   :language: dockerfile

Running ::

    podman build \
    --tag my-tutorial/my-flask-app:dev \
    .

creates a container image named ``my-tutorial/my-flask-app:dev`` that has Flask installed.

Given the following Kubernetes manifest file

.. literalinclude:: examples/flask0/play.yml
   :language: yaml

running ::

    podman kube play ./play.yml

creates a pod named ``flask`` with a container named ``flask`` running the image ``my-tutorial/my-flask-app:dev`` with a volume mounted.

`http://localhost:5000/ <http://localhost:5000/>`_ should show

> No module named 'requests'

The ``Dockerfile`` can be modified to provide the library ``requests``

.. literalinclude:: examples/flask1/Dockerfile
   :language: dockerfile

Running ::

    podman build \
    --tag my-tutorial/my-flask-app:dev \
    .

replaces the container image named ``my-tutorial/my-flask-app:dev`` with a new container image that has Flask **and** the library ``requests`` installed.

And running ::

    podman kube play --replace ./play.yml

replaces the pod named ``flask`` with a container named ``flask`` running the image ``my-tutorial/my-flask-app:dev``, now with the library ``requests`` installed, with a volume mounted.

Project Structure
-----------------

Podman can automatically match the container from the Kubernetes manifest file with the ``Dockerfile`` if the following project structure is followed. ::

    my-project/
    ├── .git
    ├── play.yaml
    └── server
        └── Dockerfile

and ``play.yaml`` includes ::

    apiVersion: v1
    kind: Pod
    metadata:
    ...
    spec:
    containers:
    - name: container
        image: server
    ...

Run ::

    podman kube play --build ./play.yml

is equivalent to run ::

    podman build \
    --tag server \
    ./server

followed by ::

    podman kube play ./play.yml
