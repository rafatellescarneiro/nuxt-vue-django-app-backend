from rest_framework.serializers import CurrentUserDefault, HiddenField, ModelSerializer
from backend.core.models import Choice, Question

from .choice import ChoiceSerializer

class QuestionSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())
    choices = ChoiceSerializer(many=True)
    
    class Meta:
        model = Question
        fields = ['id','text','creation_date','start_date','end_date','choices','owner']
    def create(self, validated_data):
        choices = validated_data.pop("choices")
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Choice.objects.create(question=question, **choice)
        return question
    
    def update(self, instance, validated_data):
        choices = validated_data.pop("choices")
        instance.text = validated_data.get("text", instance.text)
        instance.start_date = validated_data.get("start_date", instance.start_date)
        instance.end_date = validated_data.get("end_date", instance.end_date)
        instance.save()
        keep_choices = []
        for choice in choices:
            if "id" in choice.keys():
                if Choice.objects.get(id=choice['id']).exists():
                    c = Choice.objects.get(id=choice['id'])
                    c.choice_text = choice.get('choice_text', c.choice_text)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c= Choice.objects.create(question=instance, **choice)
                keep_choices.append(c.id)
        for choice in instance.choices.all():
            if choice.id not in keep_choices:
                choice.delete()
                
        return instance