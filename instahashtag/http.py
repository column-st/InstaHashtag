import json
from abc import ABC, abstractmethod
from typing import Any

import aiohttp as aiohttp_module
import requests as requests_module

from . import utils


class endpoints:
    """API endpoints."""

    tag = "https://apidisplaypurposes.com/tag/{}"
    graph = "https://apidisplaypurposes.com/graph/{}"
    maps = "https://apidisplaypurposes.com/local/?bbox={},{},{},{}&zoom={}"


class Base(ABC):
    """Base class that properly processes and calls the API.

    Allows one to "plug-and-play" with other request libraries with ease. If one wants to,
    they may inherit from this class and overwrite the abstract :py:func:`call` method.

    Example
        While the module ``httpx`` is not supported out of the box, one may inherit from the
        :py:class:`Base` class and utilize it.

        .. code-block:: python

            from instahashtag.http import Base
            import httpx

            class httpx_io(Base):
                def call(self):
                    req = httpx.get(self.endpoint, headers=self.headers)
                    resp = req.text

                    # Note that self.process is just a simple wrapper for 'json.loads'.
                    # One has the option to also overwrite this to catch any extra error(s),
                    # or run processes on the data.
                    return self.process(resp)

            class httpx_aio(Base):
                async def call(self):
                    async with httpx.AsyncClient() as client:
                        req = await client.get(self.endpoint, headers=self.headers)

                    resp = req.text
                    return self.process(resp)

            def io():
                tag = httpx_io.tag(hashtag="instagram")
                graph = httpx_io.graph(hashtag="instagram")
                maps = httpx_io.maps(
                    x1=-80.48712034709753,
                    y1=25.750749758162012,
                    x2=-79.82794065959753,
                    y2=25.854604964203453,
                    zoom=12,
                )

            def aio():
                tag = await httpx_io.tag(hashtag="instagram")
                graph = await httpx_io.graph(hashtag="instagram")
                maps = await httpx_io.maps(
                    x1=-80.48712034709753,
                    y1=25.750749758162012,
                    x2=-79.82794065959753,
                    y2=25.854604964203453,
                    zoom=12,
                )

    """

    def __init__(self, endpoint: str, headers: dict) -> None:
        self.endpoint = endpoint
        self.headers = headers

    @abstractmethod
    def call(self) -> NotImplemented:  # pragma: no cover
        """Abstract method that needs to be written to query the API endpoint."""
        raise NotImplementedError

    @staticmethod
    def process(resp: str) -> dict:
        """Processes the reply returned back by :py:data:`tag`, :py:data:`graph`, and :py:data:`maps`.

        The current implementation of this function is a simple ``json.loads(resp)``, returning
        back a Python dictionary object. However, one may chose to overwrite this function to
        process the data in some more meaningful way.
        """
        return json.loads(resp)

    @classmethod
    def tag(cls, hashtag: str) -> Any:
        """Sends an API request to the ``tag`` endpoint."""

        endpoint = endpoints.tag.format(hashtag)
        headers = utils.generate_header(hashtag=hashtag)

        obj = cls(endpoint, headers)
        return obj.call()

    @classmethod
    def graph(cls, hashtag: str) -> Any:
        """Sends an API request to the ``graph`` endpoint."""

        endpoint = endpoints.graph.format(hashtag)
        headers = utils.generate_header(hashtag=hashtag)

        obj = cls(endpoint, headers)
        return obj.call()

    @classmethod
    def maps(cls, x1: float, y1: float, x2: float, y2: float, zoom: int) -> Any:
        """Sends an API request to the ``maps`` endpoint."""

        endpoint = endpoints.maps.format(x1, y1, x2, y2, zoom)
        headers = utils.generate_header(hashtag=None)

        obj = cls(endpoint, headers)
        return obj.call()


class Requests(Base):
    """Class that utilitizes the ``request`` module to make API request."""

    def call(self):
        req = requests_module.get(url=self.endpoint, headers=self.headers)
        resp = req.text

        return self.process(resp)


class Aiohttp(Base):
    """Class that utilitizes the ``aiohttp`` module to make API request."""

    async def call(self):
        async with aiohttp_module.ClientSession(headers=self.headers) as session:
            async with session.get(self.endpoint) as response:
                resp = await response.text()

        return self.process(resp)
