import onemind.macrobrain as mb

def test_macrobrain_basic_import():
    # Minimal deterministic test: import actual modules present
    from onemind.macrobrain import subsystem as _sub
    assert _sub is not None
