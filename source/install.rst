Install
=======

Visit `Installing Podman Desktop <https://podman-desktop.io/docs/installation>`_ section from the `Podman Desktop documentation <https://podman-desktop.io/docs/>`_ for the steps to install `Podman Desktop`_` on Windows, macOS, and GNU/Linux.

On Windows and macOS, `Podman Desktop`_` will, by default, create a `Podman machine`_ because Windows and macOS cannot run containers natively.

On Windows, you can use any Windows Subsystem for Linux (`WSL`_) to run Podman and have Podman Desktop managing Podman via SSH. The next section will provide more details for this.

Configure Remote Access
-----------------------

1.  Enable remote connection on Podman Desktop's ``Settings``, ``Preferences``, ``Extension: Podman``.

2.  Generate a SSH key on that you use, for example, the Windows machine.

    .. code:: bash

        ssh-keygen -t ed25519

3.  On the GNU/Linux remote machine, install the SSH server.

4.  On the GNU/Linux remote machine, start and enable the SSH server.

5.  Copy the SSH key to ``~/.ssh/authorized_keys`` from the GNU/Linux remote machine.

6.  Test the SSH connection from the Windows machien to the GNU/Linux remote machine.

7.  On the GNU/Linux remote machine, enable Podman's socket.

    .. code:: bash

        systemctl enable --user podman.socket
        systemctl start --user podman.socket

8.  On the GNU/Linux remote machine, confirm that the Podman's socket is enabled.

    .. code:: bash

        systemctl status --user podman.socket

9.  Add the connection to the remote Podman.

    On the Windows machine, use `PowerShell`_ to run

    .. code:: powershell

        podman system connection `
        add $env:username `
        --identity c:\Users\$env:username\.ssh\id_ed25519 `
        ssh://$env:username@localhost:22/run/user/1000/podman/podman.sock

10. Confirm that the connection to the remote Podman was created.

    .. code:: powershell

        podman system connection ls
