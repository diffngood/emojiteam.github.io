from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class ChatConsumer(JsonWebsocketConsumer):

    # SQUARE_GROUP_NAME = "square"
    # groups = [SQUARE_GROUP_NAME]

    def __init__(self):
        super().__init__()
        # 인스턴스 변수는 생성자 내에서 정의합니다.
        # 인스턴스 변수 group_name 추가
        self.group_name = ""

    # 웹소켓 클라이언트가 접속을 요청할 때, 호출
    def connect(self):
        user = self.scope["user"]
        if not user.is_authenticated:
            self.close()
        else:
            room_pk = self.scope["url_route"]["kwargs"]["room_pk"]

            self.group_name = f"chat-{room_pk}"

            async_to_sync(self.channel_layer.group_add)(
                self.group_name,
                self.channel_name
            )
            self.accept()

    # 웹소켓 클라이언트와의 접속이 끊겼을 때, 호출
    def disconnect(self, code):
        if self.group_name:
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name, self.channel_name
            )

    def receive_json(self, content, **kwargs):

        user = self.scope["user"]

        _type = content["type"]

        if _type == "chat.message":
            message = content["message"]
            sender = user.username
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "chat.message",
                    "message": message,
                    "sender": sender,
                },
            )
        else:
            print(f"Invalid message type : {_type}")

    def chat_message(self, message_dict):
        self.send_json({
            "type": "chat.message",
            "message": message_dict["message"],
            "sender": message_dict["sender"],
        })
