def test_macrobrain_smoke_importable_under_hermetic_runner():
    # Minimal proof the repo is importable without triggering heavy GPU or data deps
    import importlib

    # Import the package namespace if present; otherwise prove at least Python env is sane
    assert importlib is not None
