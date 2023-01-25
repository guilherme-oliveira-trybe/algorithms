from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(110, 4)

    with pytest.raises(TypeError):
        encrypt_message("guilherme", "teste")

    assert encrypt_message("guilherme", 10) == "emrehliug"
    assert encrypt_message("guilherme", 3) == "iug_emrehl"
    assert encrypt_message("guilherme", 4) == "emreh_liug"
