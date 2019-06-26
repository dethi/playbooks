#!/usr/bin/env python3
import os
from datetime import datetime

from algoliasearch.search_client import SearchClient


def main():
    client = SearchClient.create(
        os.getenv("ALGOLIA_APP_ID"), os.getenv("ALGOLIA_APP_SECRET")
    )
    index = client.init_index("random_events")

    try:
        res = index.save_object(
            {"msg": "Generated events", "date_time": datetime.now()},
            {"autoGenerateObjectIDIfNotExist": True},
        )
        print(res)
    except:
        print("Couldn't create objects")


if __name__ == "__main__":
    main()
