class Enviador:
    def enviar(self, remetente, destinatario, titulo, mensagem):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente não é válido!!!')
        return remetente


class EmailInvalido(Exception):
    pass