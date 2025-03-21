Pod and Network
===============

.. mermaid::
   :align: center
   :alt: Diagram of network.
   :caption: Diagram of network.

    graph LR;
        browser[Web browser] --> flask[Flask];
        flask .-> postgres[PostgreSQL];

        subgraph pod[Pod]
        flask
        postgres
        end

        subgraph host[Host]
        browser
        end

