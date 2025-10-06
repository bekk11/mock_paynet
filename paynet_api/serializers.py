from rest_framework import serializers


class TransactionFieldsSerializer(serializers.Serializer):
    clientid = serializers.CharField()
    amount = serializers.IntegerField()


class TransactionParamsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    time = serializers.IntegerField()
    fields = TransactionFieldsSerializer()
    service_id = serializers.CharField()


class PaynetRequestSerializer(serializers.Serializer):
    jsonrpc = serializers.CharField()
    method = serializers.CharField()
    token = serializers.CharField(allow_blank=True)
    id = serializers.IntegerField()
    params = TransactionParamsSerializer()


class ResponseItemSerializer(serializers.Serializer):
    key = serializers.CharField()
    labelRu = serializers.CharField()
    labelUz = serializers.CharField()
    value = serializers.CharField(allow_null=True)


class TransactionResultSerializer(serializers.Serializer):
    transactionId = serializers.CharField()
    status = serializers.CharField()
    statusText = serializers.CharField()
    time = serializers.IntegerField()
    response = ResponseItemSerializer(many=True)


class PaynetResponseSerializer(serializers.Serializer):
    jsonrpc = serializers.CharField()
    id = serializers.CharField()
    result = TransactionResultSerializer()
