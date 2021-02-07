import pytest
from instahashtag import Maps


class Test_Tag_sync:
    def test_init(self):
        maps = Maps(
            x1=-80.48712034709753,
            y1=25.750749758162012,
            x2=-79.82794065959753,
            y2=25.854604964203453,
            zoom=12,
        )

    def test_init_nonexisting_map(self):
        maps = Maps(
            x1=0,
            y1=0,
            x2=1,
            y2=1,
            zoom=12,
        )

    def test_tags_gt(self):
        maps = Maps(
            x1=-80.48712034709753,
            y1=25.750749758162012,
            x2=-79.82794065959753,
            y2=25.854604964203453,
            zoom=12,
        )
        largest = max(maps.tags)


class Test_Tag_async:
    @pytest.mark.asyncio
    async def test_init(self):
        maps = Maps(
            x1=-80.48712034709753,
            y1=25.750749758162012,
            x2=-79.82794065959753,
            y2=25.854604964203453,
            zoom=12,
            aio=True,
        )
        await maps.call()
