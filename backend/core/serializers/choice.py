from rest_framework.serializers import ModelSerializer, IntegerField
from backend.core.models import Choice

class ChoiceSerializer(ModelSerializer):
    id = IntegerField(required = False)
    
    class Meta:
        model = Choice
        fields = ["id", "choice_text", "question"]
        read_only_fields = ("question",)