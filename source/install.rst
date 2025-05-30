Install
=======

Visit `Installing Podman Desktop <https://podman-desktop.io/docs/installation>`_ section from the `Podman Desktop documentation <https://podman-desktop.io/docs/>`_ for the steps to install Podman Desktop on Windows, macOS, and GNU/Linux.

On Windows and macOS, Podman Desktop will, by default, create a `Podman machine <https://podman-desktop.io/docs/podman/creating-a-podman-machine>`_ because Windows and macOS cannot run containers natively.

On Windows, you can use any `Windows Subsystem for Linux (WSL) <https://learn.microsoft.com/en-us/windows/wsl/>`_ to run Podman and have Podman Desktop managing Podman via SSH. The next section will provide more details for this.

Configure Remote Access
-----------------------

1.  Enable remote connection on Podman Desktop's ``Settings``, ``Preferences``, ``Extension: Podman``.
2.  Generate a SSH key.

    .. code:: bash

        ssh-keygen -t ed25519

3.  Copy the public SSH key to the remote machine's ``~/.ssh/authorized_keys``.
4.  On the GNU/Linux remote machine, enable Podman's socket.

    .. code:: bash

        sudo systemctl enable podman.socket
        sudo systemctl start podman.socket

5.  On the GNU/Linux remote machine, confirm that the Podman's socket is enabled.

    .. code:: bash

        systemctl status --user podman.socket

6.  Add the connection to the remote Podman.

    On the Windows machine, use `PowerShell <https://learn.microsoft.com/en-us/powershell/>`_ to run

    .. code:: powershell

        podman system connection `
        add $env:username `
        --identity c:\Users\$env:username\.ssh\id_rsa `
        ssh://$env:username@localhost:22/run/user/1000/podman/podman.sock

    as described in `Podman Remote clients for macOS and Windows <https://github.com/containers/podman/blob/main/docs/tutorials/mac_win_client.md>`_.

7.  Optionally, set the remote Podman as the default.

    On the Windows machine, use `PowerShell <https://learn.microsoft.com/en-us/powershell/>`_ to run

    .. code:: powershell

        podman system connection default $env:username