def test_imports() -> None:
    import torchxai

    assert hasattr(torchxai, "__version__")
