import onemind.macrobrain as mb

def test_macrobrain_basic_import():
    # Minimal deterministic test: import key modules
    from onemind.macrobrain import signals as _signals
    from onemind.macrobrain import processors as _proc
    assert _signals is not None
    assert _proc is not None
