class Wallet:
    def __init__(self, pubkey: str):
        self.pubkey = pubkey

    def get_invoice_url(self, amount: int, comment: str):
        return f'https://oplata.qiwi.com/create?publicKey={self.pubkey}&amount={amount}&comment={comment}'
