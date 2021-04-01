###
api
###

.. code-block:: python

    from instahashtag import api

Direct API call to DisplayPurposes with ``json`` returns. Support for synchronous and asynchronous
function call.

.. note::

    This module can either be used synchronous or asynchronous via the ``aio`` flag passed to each 
    of the functions below. By default ``aio`` is set to ``False``, but when setting it to ``True``
    the return will be an ``Awaitable`` that can be ``await`` to query the API.

    Example
        One may use the ``aio`` flag to dictate whether to use the function asynchronously 
        or synchronously.

        .. code-block:: python

            from instahashtag import api

            def io():
                """Uses 'requests' to send requests."""

                tag = api.tag(hashtag="instagram")
                graph = api.tag(hashtag="instagram")
                maps = api.maps(
                    x1=-80.48712034709753,
                    y1=25.750749758162012,
                    x2=-79.82794065959753,
                    y2=25.854604964203453,
                    zoom=12,
                )
                
            async def aio():
                """Uses 'aiohttp' to send requests."""

                tag = await api.tag(hashtag="instagram", aio=True)
                graph = await api.tag(hashtag="instagram", aio=True)
                maps = await api.maps(
                    x1=-80.48712034709753,
                    y1=25.750749758162012,
                    x2=-79.82794065959753,
                    y2=25.854604964203453,
                    zoom=12,
                )

----

.. automodule:: instahashtag.api
    :members:
