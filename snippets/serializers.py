from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = [
            'id',
            'highlight',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'owner',
        ]


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        view_name='snippet-detail',
        read_only=True,
        many=True,
    )

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
