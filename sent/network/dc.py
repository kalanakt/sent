"""Default Telegram data centers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class DataCenter:
    id: int
    ip: str
    port: int
    ipv6: Optional[str] = None


DEFAULT_DCS: Dict[int, DataCenter] = {
    1: DataCenter(1, "149.154.175.53", 443, "2001:b28:f23d:f001::a"),
    2: DataCenter(2, "149.154.167.51", 443, "2001:b28:f23d:f002::a"),
    3: DataCenter(3, "149.154.175.100", 443, "2001:b28:f23d:f003::a"),
    4: DataCenter(4, "149.154.167.92", 443, "2001:b28:f23d:f004::a"),
    5: DataCenter(5, "91.108.56.130", 443, "2001:b28:f23d:f005::a"),
}

TEST_DCS: Dict[int, DataCenter] = {
    1: DataCenter(1, "149.154.175.53", 443),
    2: DataCenter(2, "149.154.167.40", 443),
    3: DataCenter(3, "149.154.175.100", 443),
}


def get_dc(dc_id: int, test: bool = False) -> DataCenter:
    dcs = TEST_DCS if test else DEFAULT_DCS
    if dc_id not in dcs:
        raise ValueError(f"Unknown DC {dc_id}")
    return dcs[dc_id]
