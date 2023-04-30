from datetime import datetime


class AccountTransactions:
    def __init__(self, operations):
        self.operation_id = operations['id']
        self.operation_status = operations['state']
        self.operation_data = operations['date']
        self.amount = operations['operationAmount']['amount']
        self.currency = operations['operationAmount']['currency']['name']
        self.operation_form = operations.get('from')
        self.description = operations['description']
        self.operation_to = operations['to']

    def get_date(self):
        date_obj = datetime.strptime(self.operation_data, '%Y-%m-%dT%H:%M:%S.%f')
        return date_obj.strftime('%d.%m.%Y')

    def get_description(self):
        return self.description

    def get_from_operation(self):
        if not self.operation_form:
            return ''
        return self.operation_form[:-12] + ' ' + self.operation_form[-10:-8] + '** **** ' + self.operation_form[-4:]

    def get_to_operation(self):
        return '**' + self.operation_to[-4:]

    def get_amount(self):
        return f'{self.amount} {self.currency}'
