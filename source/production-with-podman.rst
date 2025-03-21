Production with Podman
======================

In the GNU/Linux world, the way to manage the GNU/Linux system and services running on it is using `systemd <https://systemd.io/>`_. For example, the cron job scheduler in your machine is probably configured using systemd. ::

    sudo systemctl status cron

should return something like ::

    ● cron.service - Regular background program processing daemon
         Loaded: loaded (/usr/lib/systemd/system/cron.service; enabled; preset: enabled)
         Active: active (running) since Wed 2025-03-19 16:19:26 CET; 4h 57min ago
     Invocation: 71415737d80c4dccbcb1313dca53b9f6
           Docs: man:cron(8)
       Main PID: 498 (cron)
          Tasks: 1 (limit: 9358)
         Memory: 496K
         CGroup: /system.slice/cron.service
                 └─498 /usr/sbin/cron -f -P
                 
Podman offers the option to use systemd to manage the pods using a superset of systemd's unit files called Quadlet files. Quadlet files can be used for

- `container <https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html#container-units-container>`_
- `kube <https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html#kube-units-kube>`_
- `pod <https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html#pod-units-pod>`_
- `volume <https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html#volume-units-volume>`_
- `network <https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html#network-units-network>`_
- `build <https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html#build-units-build>`_
- `image <https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html#image-units-image>`_

Because we have been using a Kubernetes manifest file (``play.yml``) for development, we can re-use it for production.

Workflow
--------

Example
^^^^^^^

::

    [Unit]
    Description=A kubernetes yaml based service
    Before=local-fs.target

    [Kube]
    Yaml=/opt/k8s/deployment.yml

    [Install]
    # Start by default on boot
    WantedBy=multi-user.target default.target


