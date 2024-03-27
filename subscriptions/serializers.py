from rest_framework import serializers
from core.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('channel', )

    def create(self, validated_data):

        # --------------- uncomment this in case yu want to use url params instead of req.body
        # channelId = self.context.get('request').parser_context.get('kwargs').get(
        #     'channelId')        
        validated_data['subscriber'] = self.context.get('request').user
        return super().create(validated_data)
