import pytest
from instahashtag import Graph


class Test_Graph_sync:
    def test_init(self):
        graph = Graph("miami")

    def test_init_nonexisting_hashtag(self):
        graph = Graph("random_tag_that_does_not_exist")


class Test_Graph_async:
    @pytest.mark.asyncio
    async def test_init(self):
        graph = Graph("miami", aio=True)
        await graph.call()
