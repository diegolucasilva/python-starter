import redisclient

def test_validate(monkeypatch):
    monkeypatch.setenv("CHUNK_SIZE","10")
    redisclient.scanClean()