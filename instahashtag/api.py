from typing import Union, Awaitable

from . import http


def tag(hashtag: str, aio: bool = False) -> Union[dict, Awaitable]:
    """Sends a request to the server.

    Args:
        hashtag: Hashtag to retrieve info from.
        aio: If set to ``True`` will return a Future for use with ``await`` keyword. Defaults to ``False``.

    Return:
        Dictionary with given data (see Notes below).

    Note:
        The return dictionary follows the following format:

        .. code-block:: python

            {
                geo: [float, float],
                rank: int,
                results: [
                    {
                        absRelevance: float,
                        geo: [float, float],
                        media_count: int,
                        rank: int,
                        relevance: int,
                        tag: str
                    }
                    ...
                ],
                tag: str,
                tagExists: bool
            }
    """

    if aio:
        return http.Aiohttp.tag(hashtag=hashtag)
    else:
        return http.Requests.tag(hashtag=hashtag)


def graph(hashtag: str, aio: bool = False) -> Union[dict, Awaitable]:
    """Generates graphing query to send to the server.

    Args:
        hashtag: Hashtag to retrieve info from.
        aio: If set to ``True`` will return a Future for use with ``await`` keyword. Defaults to ``False``.

    Return:
        Dictionary with given data (see Notes below).

    Note:
        The return dictionary follows the following format:

        .. code-block:: python

            {
                edges: [
                    {
                        a: str,
                        b: str,
                        id: str,
                        weight: float
                    }
                    ...
                ],
                exists: bool,
                nodes: [
                    id: str,
                    relevance: float,
                    weight: float,
                    x: float,
                    y: float
                ],
                query: string,
                root_pos: [float, float]
            }
    """

    if aio:
        return http.Aiohttp.graph(hashtag=hashtag)
    else:
        return http.Requests.graph(hashtag=hashtag)


def maps(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    zoom: float = 1,
    aio: bool = False,
) -> Union[dict, Awaitable]:
    """Generates graphing query to send to the server.

    Args:
        x1: Top left x-coordinate corner of the map.
        y1: Top left y-coordinate corner of the map.
        x2: Bottom right x-coordinate corner of the map.
        y2: Bottom right y-coordinate corner of the map.
        zoom: Number from 2 to 16 that designates the zoom factor.
        aio: If set to ``True`` will return a Future for use with ``await`` keyword. Defaults to ``False``.

    Return:
        Dictionary with given data (see Notes below).

    Note:
        The return dictionary follows the following format:

        .. code-block:: python

            {
                count: int
                tags: [
                    {
                        "centroid": [
                            0: float
                            1: float
                        ],
                        tag: str,
                        weight: int
                    }
                    ...
                ]
            }
    """

    if aio:
        return http.Aiohttp.maps(x1=x1, y1=y1, x2=x2, y2=y2, zoom=zoom)
    else:
        return http.Requests.maps(x1=x1, y1=y1, x2=x2, y2=y2, zoom=zoom)
