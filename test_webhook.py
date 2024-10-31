from flask import Flask, request, jsonify
import loko_client
from loko_client.rest import ApiException
from pprint import pprint


# Defining the host is optional and defaults to https://api.lokopay.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = loko_client.Configuration(
    host = "https://api-test.lokopay.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: publishableKeyAuth
configuration.api_key['publishableKeyAuth'] = "owgX7UqW96sxaG/3KF6L+SzWy2kWPCcUm67tem+MDB4="
configuration.secret_key = "xSJ/2AteaZT4bEw5VY7bgJ6vImNJVdWqS0UtCZ9epZgs1KsiTE6CKwmiGnj2v6b/MWo9vnBxJVLEyQn/IRSX5A=="

api_client = loko_client.ApiClient(configuration)
webhook_event_api = loko_client.WebhookEventApi(api_client)

app = Flask(__name__)

request_url = "https://405d-96-45-190-72.ngrok-free.app/webhook"


@app.route('/webhook', methods=['POST'])
def webhook():
    # 获取请求的原始 body 数据
    body_str = request.get_data(as_text=True)  # 以字符串形式获取
    # 获取请求的 JSON 数据（如果是 JSON 格式）
    json_data = request.get_json()

    # 获取请求的 headers
    headers = request.headers
    # 获取特定的 header，例如 "loko-signature"
    loko_signature = headers.get("loko-signature")

    res, err = webhook_event_api.retrieve(request_url, body_str, loko_signature)
    if res is not None:
        # 处理数据
        event_type = res.get("type")
        if event_type in [loko_client.constants.WEBHOOK_EVENT_TYPE_PAYMENT_DEPOSITED, loko_client.constants.WEBHOOK_EVENT_TYPE_PAYMENT_EXPIRED, loko_client.constants.WEBHOOK_EVENT_TYPE_PAYMENT_FAILED]:
            payment = api_client.deserialize_obj(res.get("data"), "Payment")
            pprint(payment)
        elif event_type in [loko_client.constants.WEBHOOK_EVENT_TYPE_PAYOUT_SUCCEEDED, loko_client.constants.WEBHOOK_EVENT_TYPE_PAYOUT_PENDING, loko_client.constants.WEBHOOK_EVENT_TYPE_PAYOUT_FAILED]:
            payout = api_client.deserialize_obj(res.get("data"), "Payout")
            pprint(payout)
    else :
        pprint(err)

    return jsonify({"success":0}), 200

if __name__ == '__main__':
    app.run(port=5000)