####
http
####

.. code-block:: python

    from instahashtag.http import Base, Requests, Aiohttp

Low-level HTTP calls to DisplayPurposes with ``json`` returns. Allows customization with 
"plug-and-play" support for any other Python HTTP request library. Comes out of the box
with support for both the  ``requests`` and ``aiohttp`` packages.

.. note:: 

    The classes documented here are not intended to be used for querying the API- they are here
    to allow customization support for anyone looking to use their own HTTP request library to
    send requests to the API. 

    If you are looking for retrieving back the raw ``json`` objects without carying much about
    implementation, check out the documentations for the :ref:`api` module.

----

.. autoclass:: instahashtag.http.endpoints

    .. code-block:: python

        class endpoints:
            tag = "https://apidisplaypurposes.com/tag/{}"
            graph = "https://apidisplaypurposes.com/graph/{}"
            maps = "https://apidisplaypurposes.com/local/?bbox={},{},{},{}&zoom={}"

.. autoclass:: instahashtag.http.Base

    .. automethod:: instahashtag.http.Base.call

    .. automethod:: instahashtag.http.Base.process

    .. automethod:: instahashtag.http.Base.tag

    .. automethod:: instahashtag.http.Base.graph

    .. automethod:: instahashtag.http.Base.maps

----

The classes below are the out-of-the-box implementations used by the higher layers.

.. autoclass:: instahashtag.http.Requests

.. autoclass:: instahashtag.http.Aiohttp
