from rest_framework import serializers
from .models import Movie

class MovieModelSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField(required=False)

    class Meta:
        model = Movie
        fields = '__all__'

    def validate(self, attrs):
        if self.instance is None and 'video_file' not in attrs:
            raise serializers.ValidationError({
                'video_file': 'This field is required when creating a new movie.'
            })
        return attrs