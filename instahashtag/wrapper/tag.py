from typing import List

from .. import api


class TagResult:
    def __init__(
        self,
        tag: str,
        rank: int,
        geo: List[float],
        media_count: int,
        relevance: int,
        absRelevance: float,
    ) -> None:
        """Object that represents the individual items inside the ``Tag.results`` list.

        Attributes:
            tag: Related hashtag.

                .. code-block:: python

                    result.tag # >>> miamibeach

            rank: Ranking of the tag.

                .. code-block:: python

                    result.rank # >>> 74

            geo: List of floats that contains coordinates to the hashtag.

                .. code-block:: python

                    result.geo # >>> [25.819434533299013, -80.16981253812398]

            media_count: Number of posts in the hashtag.

                .. code-block:: python

                    result.media_count # >>> 4329283

            relevance: Relevance of the hashtag to the queried hashtag.

                .. code-block:: python

                    result.relevance # >>> 99

            absRelevance: Absolute relevance to the queried hashtag.

                .. code-block:: python

                    result.absRelevance # >>> 0.0060874452062492975
        """
        self.tag = tag
        self.rank = rank
        self.geo = geo
        self.media_count = media_count
        self.relevance = relevance
        self.absRelevance = absRelevance

    def __gt__(self, other: "Result") -> bool:
        """Allows comparisson of :py:class:`Result` objects by their ``rank``.

        Note:
            This function allows the user to utilize the Python built-in functions.

            .. code-block:: python

                from instahashtag import Tag

                tag = Tag("miami")

                min(tag.results)
                max(tag.results)
                sort(tag.results)

        """
        return self.rank > other.rank

    def __repr__(self) -> str: # pragma: no cover
        return "Result(tag={}, rank={}, geo={}, media_count={}, relevance={}, absRelevance={})".format(
            self.tag,
            self.rank,
            self.geo,
            self.media_count,
            self.relevance,
            self.absRelevance,
        )

    def __str__(self) -> str: # pragma: no cover
        return self.__repr__()


class Tag:
    def __init__(self, hashtag: str, aio: bool = False) -> None:
        """Initializes a new Tag object.

        .. code-block:: python

            from instahashtag import Tag

            tag = Tag("miami")

        Attributes:
            hashtag: Hashtag that was used to retrieve information from.

               .. code-block:: python

                    tag.hashtag # >>> miami

            geo: List containing two float coordinates relating to the hashtag.

                .. code-block:: python

                    tag.geo # >>> [25.821117872941034, -80.20722606661316]

            rank: Integer representation of the rank of the hashtag relative to others.

                .. code-block:: python

                    tag.rank # >>> 83

            exists: Bool representation of whether or not the passed hashtag exists.

                .. code-block:: python

                    tag.exists # >>> True

            results: List of :py:class:`TagResult` containing information on related hashtags.

                .. code-block:: python

                    tag.results # >>> [Result(tag=..., rank=..., geo=[...,...], media_count=..., relevance=..., abs_relevance=...), ...]
                    result = tag.results[0]

                .. autoclass:: instahashtag.wrapper.tag.TagResult

                    .. autofunction:: instahashtag.wrapper.tag.TagResult.__gt__
        """

        self.hashtag = hashtag
        self.geo = None
        self.rank = None
        self.results = None
        self.exists = None

        if not aio:
            self.data = api.tag(hashtag=self.hashtag)
            self.process()

    async def call(self) -> None:
        """Asynchronously queries the API.

        See note on the top of the :ref:`wrapper` documentation.
        """
        self.data = await api.tag(hashtag=self.hashtag, aio=True)
        self.process()

    def process(self) -> None:
        self.geo = self.data.get("geo", None)
        self.rank = self.data.get("rank", None)
        self.exists = self.data.get("tagExists", None)

        results = self.data.get("results", [])
        if results:
            self.results = [TagResult(**r) for r in results]
        else:
            self.results = results

    def __repr__(self) -> str: # pragma: no cover
        return "Tag(hashtag={}, exists={}, rank={}, results_len={})".format(
            self.hashtag,
            self.exists,
            self.rank,
            len(self.results),
        )

    def __str__(self) -> str: # pragma: no cover
        return self.__repr__()
