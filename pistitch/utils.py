"""Tiny helper utilities for later expansion."""


def repeat_pattern(pattern_fn, times=1):
    """Return a function that applies pattern_fn multiple times.
    Placeholder for future pattern-repeat helpers.
    """

    def wrapped(*args, **kwargs):
        for _ in range(times):
            pattern_fn(*args, **kwargs)

    return wrapped
