import uuid
from datetime import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiExample
from .serializers import PaynetRequestSerializer, PaynetResponseSerializer


class PerformTransactionView(generics.GenericAPIView):
    """
    API view to handle Paynet transaction requests and return formatted response.
    """
    serializer_class = PaynetRequestSerializer

    @extend_schema(
        request=PaynetRequestSerializer,
        responses={200: PaynetResponseSerializer},
        summary="Perform Paynet Transaction",
        description="Process a Paynet transaction and return transaction details",
        examples=[
            OpenApiExample(
                'Transaction Request Example',
                value={
                    "jsonrpc": "2.0",
                    "method": "performTransaction",
                    "token": "",
                    "id": 126,
                    "params": {
                        "id": 1747317450780,
                        "time": 1747317450801,
                        "fields": {
                            "clientid": "911924138",
                            "amount": 500
                        },
                        "service_id": "11629"
                    }
                },
                request_only=True,
            ),
            OpenApiExample(
                'Transaction Response Example',
                value={
                    "jsonrpc": "2.0",
                    "id": "96ff1a0f-3b12-4278-8f90-e571c7ed267c",
                    "result": {
                        "transactionId": "23379302716",
                        "status": "0",
                        "statusText": "Проведен успешно",
                        "time": 1759198026000,
                        "response": [
                            {
                                "key": "agent_name",
                                "labelRu": "Агент",
                                "labelUz": "Agent",
                                "value": "CONTINEO ASIA"
                            },
                            {
                                "key": "clientid",
                                "labelRu": "Номер телефона",
                                "labelUz": "Telefon raqami",
                                "value": "994061744"
                            }
                        ]
                    }
                },
                response_only=True,
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        # Validate incoming request
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        # Extract request data
        params = validated_data['params']
        fields = params['fields']

        # Build response data
        response_data = {
            "jsonrpc": "2.0",
            "id": validated_data['id'],
            "result": {
                "transactionId": str(int(datetime.now().timestamp() * 1000)),
                "status": "0",
                "statusText": "Проведен успешно",
                "time": int(datetime.now().timestamp() * 1000),
                "response": [
                    {
                        "key": "agent_name",
                        "labelRu": "Агент",
                        "labelUz": "Agent",
                        "value": "CONTINEO ASIA"
                    },
                    {
                        "key": "agent_inn",
                        "labelRu": "ИНН",
                        "labelUz": "STIR",
                        "value": "305923492"
                    },
                    {
                        "key": "provider_name",
                        "labelRu": "Оператор",
                        "labelUz": "Operator",
                        "value": "Сотовая связь"
                    },
                    {
                        "key": "service_name",
                        "labelRu": "Услуга",
                        "labelUz": "Xizmat turi",
                        "value": "Проверка номера"
                    },
                    {
                        "key": "time",
                        "labelRu": "Время",
                        "labelUz": "To'lov vaqti",
                        "value": datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                    },
                    {
                        "key": "terminal_id",
                        "labelRu": "Номер терминала",
                        "labelUz": "Terminal raqami",
                        "value": "4187535"
                    },
                    {
                        "key": "transaction_id",
                        "labelRu": "Номер чека",
                        "labelUz": "Chek raqami",
                        "value": str(int(datetime.now().timestamp() * 1000))
                    },
                    {
                        "key": "clientid",
                        "labelRu": "Номер телефона",
                        "labelUz": "Telefon raqami",
                        "value": fields['clientid']
                    },
                    {
                        "key": "check_status",
                        "labelRu": "Статус номера",
                        "labelUz": "Raqam statusi",
                        "value": None
                    },
                    {
                        "key": "provider_id_new",
                        "labelRu": "Провайдер ID",
                        "labelUz": "Provayder ID",
                        "value": "45"
                    },
                    {
                        "key": "provider_name_real",
                        "labelRu": "Наименование оператора",
                        "labelUz": "Operator nomi",
                        "value": "UzMobile"
                    },
                    {
                        "key": "service_id_new",
                        "labelRu": "Сервис ID",
                        "labelUz": "Servis ID",
                        "value": "4987"
                    },
                    {
                        "key": "service_name_real",
                        "labelRu": "Наименование сервиса",
                        "labelUz": "Xizmat nomi",
                        "value": "Проверка номера"
                    },
                    {
                        "key": "limit",
                        "labelRu": "Лимит пополнения в месяц",
                        "labelUz": "Oyiga to`ldirish cheklovi",
                        "value": None
                    },
                    {
                        "key": "max_amount",
                        "labelRu": "Максимальная сумма",
                        "labelUz": "Maksimal summa",
                        "value": None
                    },
                    {
                        "key": "agent_commission",
                        "labelRu": "Комиссия агента",
                        "labelUz": "Agent komissiyasi",
                        "value": "0"
                    }
                ]
            }
        }

        # Validate response format
        response_serializer = PaynetResponseSerializer(data=response_data)
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
