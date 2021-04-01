#######
wrapper
#######

.. code-block:: python

    from instahashtag import Tag, Graph, Maps

Complete object-oriented wrappers over the API. Allows quering the server and accessing
the return information directly via the Python objects.

.. note::

    For all of the classes below if the ``aio`` flag is ``False`` then the object will 
    automatically query the API without needing further action. However, if the ``aio`` 
    flag is set to ``True`` one must ``await`` the :py:func:`call` function associated
    with the object to make the query to the server.

    .. code-block:: python

        from instahashtag import Maps
        import asyncio

        async def main():
            tag = Maps(
                x1=-80.48712034709753,
                y1=25.750749758162012,
                x2=-79.82794065959753,
                y2=25.854604964203453,
                zoom=12,
                aio=True
            )
            await tag.call()

-----

.. toctree::
  :caption: Packages
  :glob:

  wrapper/tag
  wrapper/graph
  wrapper/maps
