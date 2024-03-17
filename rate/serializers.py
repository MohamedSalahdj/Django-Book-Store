from rest_framework import serializers
from rate.models import Rate
class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rate
        fields='__all__'
        extra_kwargs = {'book': {'required': True},'user': {'required': True}}
    
    # def validate(self,data):
    #     if data['rate']!=None:
    #         if data['rate'] > 5 or data['rate'] < 1 :
    #             raise serializers.ValidationError({'error':"rate should be between 1 and 5"})
    #     return data
        


 