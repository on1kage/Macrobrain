import onemind.macrobrain as mb

def test_macrobrain_basic_import_hermetic():
    # Only verify the package namespace is importable hermetically
    import importlib
    assert importlib is not None
    assert mb is not None
