from utils.receiving_invoices import get_invoice


def test_get_invoices():
    assert len(get_invoice()) == 5
