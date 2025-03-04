Install
=======

Visit `Installing Podman Desktop <https://podman-desktop.io/docs/installation>` section from the `Podman Desktop documentation <https://podman-desktop.io/docs/>`_ for the steps to install Podman Desktop on Windows, macOS, and GNU/Linux.

Podman Desktop can manage remote Podman connections via SSH. On Windows and macOS, Podman Desktop is bundled with the `Podman machine <https://podman-desktop.io/docs/podman/creating-a-podman-machine>`_ but it is recommended to configure Podman on the machine you are using instead of use the default Podman machine.

Configure Remote Access
-----------------------

1. Enable remote connection on Podman Desktop's settings.
2. On Windows, generate a SSH key. ::

    ssh-keygen -t ed25519

3. Copy the SSH key to the remote machine.
4. On the remote machine, enable Podman's socket. ::

    sudo systemctl enable podman.socket
    sudo systemctl start podman.socket

5. On the remote machine, confirm that the Podman's socket is enabled. ::

    systemctl status --user podman.socket

6. On Windows, add the connection to the remote Podman as described in `Podman Remote clients for macOS and Windows <https://github.com/containers/podman/blob/main/docs/tutorials/mac_win_client.md>`_. ::

    podman system connection add baude --identity c:\Users\baude\.ssh\id_rsa ssh://192.168.122.1/run/user/1000/podman/podman.sock
