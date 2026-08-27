from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_valid: mock.Mock,
        mocked_has_internet: mock.Mock
) -> None:
    mocked_has_internet.return_value = True
    mocked_valid.return_value = True
    assert can_access_google_page("google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_with_invalid_url(
        mocked_valid: mock.Mock,
        mocked_has_internet: mock.Mock
) -> None:
    mocked_has_internet.return_value = True
    mocked_valid.return_value = False
    assert can_access_google_page("valid.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_with_only_valid_url(
        mocked_valid: mock.Mock,
        mocked_has_internet: mock.Mock
) -> None:
    mocked_has_internet.return_value = False
    mocked_valid.return_value = True
    assert can_access_google_page("valid.com") == "Not accessible"
