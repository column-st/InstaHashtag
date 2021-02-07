import pytest
from instahashtag import Tag


class Test_Tag_sync:
    def test_init(self):
        tag = Tag("miami")

    def test_init_nonexisting_hashtag(self):
        tag = Tag("random_tag_that_does_not_exist")

    def test_tags_gt(self):
        tag = Tag("miami")
        largest = max(tag.results)

class Test_Tag_async:
    @pytest.mark.asyncio
    async def test_init(self):
        tag = Tag("miami", aio=True)
        await tag.call()
