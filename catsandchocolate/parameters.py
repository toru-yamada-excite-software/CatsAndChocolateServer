from rest_framework import serializers


class GenerateItemsParameters(object):
    def __init__(self, title: str, count: int):
        self.title = title
        self.count = count


class GenerateItemsParametersSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    count = serializers.IntegerField(min_value=0, max_value=100)

    def create(self, validated_data):
        return GenerateItemsParameters(**validated_data)


class GenerateEventsParameters(object):
    def __init__(self, title: str, count: int):
        self.title = title
        self.count = count


class GenerateEventsParametersSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    count = serializers.IntegerField(min_value=0, max_value=100)

    def create(self, validated_data):
        return GenerateEventsParameters(**validated_data)


class EvaluateSolutionParameters(object):
    def __init__(self, event: str, solution: str):
        self.event = event
        self.solution = solution


class EvaluateSolutionParametersSerializer(serializers.Serializer):
    event = serializers.CharField()
    solution = serializers.CharField()

    def create(self, validated_data):
        return EvaluateSolutionParameters(**validated_data)


class FindSolutionParameters(object):
    def __init__(self, title: str, event: str, items: list[str], number_to_use: int):
        self.title = title
        self.event = event
        self.items = items
        self.number_to_use = number_to_use


class FindSolutionParametersSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    event = serializers.CharField()
    items = serializers.ListField(child=serializers.CharField())
    number_to_use = serializers.IntegerField(min_value=1, max_value=3)

    def create(self, validated_data):
        return FindSolutionParameters(**validated_data)
