from typing import List

from .. import api


class MapsTag:
    """Object that represents the individiual items inside the ``Maps.tags`` list.

    Attributes:
        centroid: List of floats that contains the location of the tag in the map (lon, lat).

            .. code-block::

                tag.centroid # >>> [25.801775593361942, -80.20252247848369]

        tag: Hashtag name.

            .. code-block::

                tag.tag # >>> igersmiami

        weight: Weight of the hashtag on the map.

            .. code-block::

                tag.weight # >>> 49
    """

    def __init__(self, centroid: List[float], tag: str, weight: int) -> None:
        self.centroid = centroid
        self.tag = tag
        self.weight = weight

    def __gt__(self, other: "Result") -> bool:
        """Allows comparisson of :py:class:`MapsTags` objects by their ``weight``.

        Note:
            This function allows the user to utilize the Python built-in functions.

            .. code-block:: python

                from instahashtag import Maps

                # Coordinates designate to Miami, FL.
                maps = Maps(
                    x1=-80.48712034709753,
                    y1=25.750749758162012,
                    x2=-79.82794065959753,
                    y2=25.854604964203453,
                    zoom=12
                )

                min(maps.tags)
                max(maps.tags)
                sort(maps.tags)

        """
        return self.weight > other.weight

    def __repr__(self) -> str:  # pragma: no cover
        return "MapTag(tag={}, centroid={}, weight={})".format(
            self.tag,
            self.centroid,
            self.weight,
        )

    def __str__(self) -> str:  # pragma: no cover
        return self.__repr__()


class Maps:
    def __init__(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        zoom: int,
        aio: bool = False,
    ) -> None:
        """Initializes a new map object.

        .. code-block:: python

            from instahashtag import Maps

            # Coordinates designate to Miami, FL.
            maps = Maps(
                x1=-80.48712034709753,
                y1=25.750749758162012,
                x2=-79.82794065959753,
                y2=25.854604964203453,
                zoom=12
            )

        Attributes:
            x1: Top left x-coordinate corner of the map.

                .. code-block:: python

                    maps.x1 # >>> -80.48712034709753

            y1: Top left y-coordinate corner of the map.

                .. code-block:: python

                    maps.y1 # >>> 25.750749758162012

            x2: Bottom right x-coordinate corner of the map.

                .. code-block:: python

                    maps.x2 # >>> -79.82794065959753

            y2: Bottom right y-coordinate corner of the map.

                .. code-block:: python

                    maps.y2 # >>> 25.854604964203453

            zoom: Number from 2 to 16 that designates the zoom factor.

                .. code-block:: python

                    maps.zoom # >>> 12

            count: Number of hashtags in the resulting query.

                .. code-block:: python

                    maps.count # >>> 91

            tags: List of hashtags.

                .. code-block:: python

                    maps.tags # >>> [MapTag(tag=..., centroid=[..., ...], weight=...), ...]
                    tag = maps.tags[0]

                .. autoclass:: instahashtag.wrapper.maps.MapsTag

                    .. autofunction:: instahashtag.wrapper.maps.MapsTag.__gt__

        """

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.zoom = zoom

        if not aio:
            self.data = api.maps(
                x1=self.x1,
                y1=self.y1,
                x2=self.x2,
                y2=self.y2,
                zoom=self.zoom,
            )
            self.process()

    async def call(self) -> None:
        """Asynchronously queries the API.

        See note on the top of the :ref:`wrapper` documentation.
        """
        self.data = await api.maps(
            x1=self.x1,
            y1=self.y1,
            x2=self.x2,
            y2=self.y2,
            zoom=self.zoom,
            aio=True,
        )
        self.process()

    def process(self) -> None:
        """Processes the incoming data from the API."""

        self.count = self.data.get("count", None)

        tags = self.data.get("tags", [])
        if tags:
            self.tags = [MapsTag(**t) for t in tags]
        else:
            self.tags = []

    def __repr__(self) -> str:  # pragma: no cover
        return (
            "Graph(x1={}, y1={}, x2={}, y2={}, zoom={}, count={}, tags_len={})".format(
                self.x1,
                self.y1,
                self.x2,
                self.y2,
                self.zoom,
                self.count,
                len(self.tags),
            )
        )

    def __str__(self) -> str:  # pragma: no cover
        return self.__repr__()
