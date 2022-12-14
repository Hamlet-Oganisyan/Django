from datetime import datetime

class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, self.format)

    def to_url(self, value: str) -> str:
        return value.strftime(self.format)

register_converter = (PubDateConverter, 'date')