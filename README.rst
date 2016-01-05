
==========================
Leonardo leonardo-api
==========================

API for Leonardo CMS.

Just PoC under development, not production ready yet.

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo-api

Usage
-----

This API is only generic skeleton for your APIs.

.. code-block:: python

    class MyModel:

        class Meta:
            app = 'web'

.. code-block:: bash

    http GET localhost/api/models/web.mymodel/
    ...

For customization declare ``serializer_class`` on your model::

    class MyModel:

        serializer_class = MyModelSerializer

        class Meta:
            app = 'web'


Read More
=========

* https://github.com/django-leonardo/django-leonardo
