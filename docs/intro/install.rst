.. _intro-install:

==================
Installation guide
==================

Installing py-school-match
==========================

.. _intro-install-ubuntu:

Ubuntu
---------------------

Py-school-match uses `graph-tool <https://graph-tool.skewed.de/>`__ for most algorithms.
You can install it by following `this <https://git.skewed.de/count0/graph-tool/wikis/installation-instructions#debian-ubuntu>`__ guide.

After this, you can simply install py-school-match with ``pip``::

    pip install py-school-match


Or by doing::

    git clone https://github.com/igarizio/py-school-match
    cd py-school-match
    python setup.py install


.. _intro-install-windows:

Windows
-------

Windows is not currently supported, but if you are still interested, I recommend using Windows Subsystem for Linux
(read `this <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`__ guide) and then configure remote interpreters via SSH (if you are using Pycharm, you can read this
`this <https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html>`__ guide).
