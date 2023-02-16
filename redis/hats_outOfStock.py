#!/usr/bin/python3
"""
OutOfStockError class
"""

import logging
import redis

logging.basicConfig()


class OutOFStockError(Exception):
    """Raised when PyHats.com is all out of today's hottest hat"""

    def buyitem(r: redis.Redis, itemid: int) -> None:
        """
        r:
          redis.Redis
        itemid: int
        """
        with r.pipeline() as pipe:
            error_count = 0
            while True:
                try:
                    # get available inventory, watching for changes
                    # related to this itemid before the transaction
                    pipe.watch(itemid)
                    nleft: bytes = r.hget(itemid, "quantity")
                    if nleft > b'0':
                        pipe.multi()
                        pipe.hincrby(itemid, 'quantity', -1)
                        pipe.hincrby(itemid, 'npurchased', 1)
                        pipe.execute()
                        break
                    else:
                        # stop watchin the itemid and raise an a break out
                        pipe.unwatch()
                        raise OutOfStockError(
                                f"sorry, {itemid} is out of stock!"
                                )

                except redis.WatchError:
                    # # Log total num. of errors by this user to buy this item,
                    # then try the same process again of WATCH/HGET/MULTI/EXEC
                    error_count += 1
                    logging.warning("watchError #%d: %s; retrying",
                                    error_count, itemid)

        return None

    
    buyitem(r, "hat:56854717")
    buyitem(r, "hat:56854717")
    buyitem(r, "hat:56854717")
    r.hmget("hat:56854717", "quantity", "npurchased")
