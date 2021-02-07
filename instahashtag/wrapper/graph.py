from .. import api


class GraphNode:
    def __init__(
        self,
        id: str,
        relevance: float,
        weight: float,
        x: float,
        y: float,
    ) -> None:
        """Object that represents the individual edges inside the ``Graph.nodes`` list.

        Attributes:
            id: Hashtag name.

                .. code-block:: python

                    node.name # >>> liv

            relevance: Relevance of the node.

                .. code-block:: python

                    node.relevance # >>> 0.5417327185029007

            weight: Weight of the node.

                .. code-block:: python

                    node.weight # >>> 0.4523809523809524

            x: Position of the node in relation to the x-axis.

                .. code-block:: python

                    node.x # >>> 0.20431805750484297

            y: Position of the node in relation to the y-axis.

                .. code-block:: python

                    node.y # >>> 0.6194782200730474
        """
        self.id = id
        self.relevance = relevance
        self.weight = weight
        self.x = x
        self.y = y

    def __repr__(self) -> str:  # pragma: no cover
        return "Node(id={}, relevance={}, weight={}, x={}, y={})".format(
            self.id,
            self.relevance,
            self.weight,
            self.x,
            self.y,
        )

    def __str__(self) -> str:  # pragma: no cover
        return self.__repr__()


class GraphEdge:
    def __init__(self, a: str, b: str, id: str, weight: int) -> None:
        """Object that represents the individual edges inside the ``Graph.edges`` list.

        Attributes:
            a: Hashtag name that represents a node in the graph.

                .. code-block:: python

                    edge.a # >>> liv

            b: Hashtag name that represents another node in the graph.

                .. code-block:: python

                    edge.a # >>> thingstodomiami

            id: Order of the connection between nodes.

                .. code-block:: python

                    edge.id # >>> liv#thingstodomiami

            weight: Weight of the edge.

                .. code-block:: python

                    edge.weight # >>> 0.44775669978922017

        Note:
            The edge object of the graph represents `which` node is connected to which other node.
        """
        self.a = a
        self.b = b
        self.id = id
        self.weight = weight

    def __repr__(self) -> str:  # pragma: no cover
        return "Edge(a={}, b={}, id={}, weight={})".format(
            self.a,
            self.b,
            self.id,
            self.weight,
        )

    def __str__(self) -> str:  # pragma: no cover
        return self.__repr__()


class Graph:
    def __init__(self, hashtag: str, aio: bool = False) -> None:
        """Initializes a new Graph object.

        .. code-block:: python

            from instahashtag import Graph

            graph = Graph("miami")

        Attributes:
            hashtag: Hashtag that was used to retrieve information from.

               .. code-block:: python

                    graph.hashtag # >>> miami

            exists: Boolean that dictates whether or not the passed hashtag exists.

               .. code-block:: python

                    graph.exists # >>> True

            root_pos: List of floats indicating where the root position of the graph is.

                .. code-block:: python

                    graph.root_post # >>> [0.4495344797287565, 0.40752168227901403]

            nodes: List of :py:class:`GraphNode` containing information on related hashtags.

                .. code-block:: python

                    graph.nodes # >>> [Node(id=..., relevance=..., weight=..., x=..., y=...), ...]
                    node = graph.nodes[0]

                .. autoclass:: instahashtag.wrapper.graph.GraphNode

            edges: List of :py:class:`GraphEdge` containing information on the connection between hashtags.

                .. code-block:: python

                    graph.edges # >>> [Edge(a=..., b=..., id=...#..., weight=...), ...]
                    edge = graph.edges[0]

                .. autoclass:: instahashtag.wrapper.graph.GraphEdge

        """

        self.hashtag = hashtag
        self.edges = None
        self.exists = None
        self.nodes = None
        self.query = None
        self.root_pos = None

        if not aio:
            self.data = api.graph(hashtag=self.hashtag)
            self.process()

    async def call(self) -> None:
        """Asynchronously queries the API.

        See note on the top of the :ref:`wrapper` documentation.
        """
        self.data = await api.graph(hashtag=self.hashtag, aio=True)
        self.process()

    def process(self) -> None:
        """Processes the incoming data from the API."""

        self.exists = self.data.get("exists", None)
        self.root_pos = self.data.get("root_pos", None)

        edges = self.data.get("edges", [])
        if edges:
            self.edges = [GraphEdge(**e) for e in edges]
        else:
            self.edges = edges

        nodes = self.data.get("nodes", [])
        if nodes:
            self.nodes = [GraphNode(**n) for n in nodes]
        else:
            self.nodes = nodes

    def __repr__(self) -> str:  # pragma: no cover
        return "Graph(hashtag={}, exists={}, root_pos={}, edges_len={}, nodes_len={})".format(
            self.hashtag,
            self.exists,
            self.root_pos,
            len(self.edges),
            len(self.nodes),
        )

    def __str__(self) -> str:  # pragma: no cover
        return self.__repr__()
