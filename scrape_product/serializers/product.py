from rest_framework import serializers


class ScrapeProductInputSerializer(serializers.Serializer):
    scrape_url = serializers.CharField(max_length=50)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
