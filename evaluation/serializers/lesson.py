from rest_framework import serializers
from evaluation.models import Lesson
from .test1 import Test1Serializer
from .test2 import Test2Serializer
from .test3 import Test3Serializer


class LessonSerializer(serializers.ModelSerializer):
    test1 = Test1Serializer(many=True)
    test2 = Test2Serializer(many=True)
    test3 = Test3Serializer(many=True)

    class Meta:
        model = Lesson
        fields = [
            'title',
            'study_text',
            'test1',
            'test2',
            'test3',
        ]
