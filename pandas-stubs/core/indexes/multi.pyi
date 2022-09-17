from typing import (
    Callable,
    Hashable,
    Literal,
    Sequence,
)

import numpy as np
from pandas.core.indexes.base import Index

from pandas._typing import (
    T1,
    DtypeArg,
    np_ndarray_bool,
)

class MultiIndex(Index):
    def __new__(
        cls,
        levels=...,
        codes=...,
        sortorder=...,
        names=...,
        dtype=...,
        copy=...,
        name=...,
        verify_integrity: bool = ...,
        _set_identity: bool = ...,
    ) -> MultiIndex: ...
    def __init__(
        self,
        levels=...,
        codes=...,
        sortorder=...,
        names=...,
        dtype=...,
        copy=...,
        name=...,
        verify_integrity: bool = ...,
        _set_identity: bool = ...,
    ) -> None: ...
    @classmethod
    def from_arrays(cls, arrays, sortorder=..., names=...) -> MultiIndex: ...
    @classmethod
    def from_tuples(cls, tuples, sortorder=..., names=...) -> MultiIndex: ...
    @classmethod
    def from_product(cls, iterables, sortorder=..., names=...) -> MultiIndex: ...
    @classmethod
    def from_frame(cls, df, sortorder=..., names=...) -> MultiIndex: ...
    @property
    def shape(self): ...
    @property  # Should be read-only
    def levels(self) -> list[Index]: ...
    def set_levels(
        self, levels, level=..., inplace: bool = ..., verify_integrity: bool = ...
    ): ...
    @property
    def codes(self): ...
    def set_codes(
        self, codes, level=..., inplace: bool = ..., verify_integrity: bool = ...
    ): ...
    def copy(self, names=..., deep: bool = ...) -> MultiIndex: ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def view(self, cls=...): ...
    def __contains__(self, key) -> bool: ...
    def dtype(self) -> np.dtype: ...
    def memory_usage(self, deep: bool = ...) -> int: ...
    def nbytes(self) -> int: ...
    def format(
        self,
        name: bool | None = ...,
        formatter: Callable | None = ...,
        na_rep: str | None = ...,
        names: bool = ...,
        space: int = ...,
        sparsify: bool | None = ...,
        adjoin: bool = ...,
    ) -> list: ...
    def __len__(self) -> int: ...
    def inferred_type(self) -> str: ...
    @property
    def values(self): ...
    def is_monotonic_increasing(self) -> bool: ...
    def is_monotonic_decreasing(self) -> bool: ...
    def duplicated(self, keep: str = ...): ...
    def fillna(self, value=..., downcast=...) -> None: ...
    def dropna(self, how: Literal["any", "all"] = ...) -> MultiIndex: ...
    def get_value(self, series, key): ...
    def get_level_values(self, level: str | int) -> Index: ...
    def unique(self, level=...): ...
    def to_frame(self, index: bool = ..., name=...): ...
    def to_flat_index(self): ...
    @property
    def is_all_dates(self) -> bool: ...
    def is_lexsorted(self) -> bool: ...
    def lexsort_depth(self): ...
    def remove_unused_levels(self): ...
    @property
    def nlevels(self) -> int: ...
    @property
    def levshape(self): ...
    def __reduce__(self): ...
    def __getitem__(self, key): ...
    def take(
        self, indices, axis: int = ..., allow_fill: bool = ..., fill_value=..., **kwargs
    ): ...
    def append(self, other): ...
    def argsort(self, *args, **kwargs): ...
    def repeat(self, repeats, axis=...): ...
    def where(self, cond, other=...) -> None: ...
    def drop(self, codes, *, level=..., errors: str = ...) -> MultiIndex: ...
    def swaplevel(self, i: int = ..., j: int = ...): ...
    def reorder_levels(self, order): ...
    def sortlevel(
        self, level: int = ..., ascending: bool = ..., sort_remaining: bool = ...
    ): ...
    def get_indexer(self, target, method=..., limit=..., tolerance=...): ...
    def get_indexer_non_unique(self, target): ...
    def reindex(self, target, method=..., level=..., limit=..., tolerance=...): ...
    def get_slice_bound(
        self, label: Hashable | Sequence[Hashable], side: str
    ) -> int: ...
    def slice_locs(self, start=..., end=..., step=...): ...
    def get_loc(self, key): ...
    def get_loc_level(self, key, level=..., drop_level: bool = ...): ...
    def get_locs(self, seq): ...
    def truncate(self, before=..., after=...): ...
    def equals(self, other) -> bool: ...
    def equal_levels(self, other): ...
    def union(self, other, sort=...): ...
    def intersection(self, other, sort: bool = ...): ...
    def difference(self, other, sort=...): ...
    def astype(self, dtype: DtypeArg | T1, copy: bool = ...) -> MultiIndex: ...
    def insert(self, loc, item): ...
    def delete(self, loc): ...
    def isin(self, values, level=...) -> np_ndarray_bool: ...

def maybe_droplevels(index, key): ...
