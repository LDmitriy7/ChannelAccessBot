import texts
from models import documents


def get_text(text_model: type[documents.Text]) -> str:
    text_doc: documents.Text = text_model.objects().first()

    if text_doc:
        return text_doc.value
    return texts.no_text_set
