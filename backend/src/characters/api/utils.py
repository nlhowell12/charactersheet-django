from characters.models import Feat
from rest_framework.response import Response
from xlrd import open_workbook


def generate_feats(feat_file):
    delete_feats()
    book = open_workbook(file_contents=feat_file.read())
    sheet = book.sheets()[0]
    rows = sheet.get_rows()
    for row in rows:
        if(row[0].ctype == 1):
            Feat.objects.create(
                feat_classification=row[0].value,
                feat_name=row[1].value,
                prerequisites=row[2].value,
                benefit=row[3].value
            )
    return Response({'Upload Succesful'})


def delete_feats():
    return Feat.objects.all().delete()
