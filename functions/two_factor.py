import twilio

def two_factor(context):
  # ランダムな6桁のコードを生成
  code = random.randint(100000, 999999)

  # ログインサービスにコードを登録
  user = context.json["user"]
  register_code_with_login_service(user, code)

  # テキストメッセージの送信にTwilioのライブラリを使用
  account = "my-account-sid"
  token = "my-token"
  client = twilio.rest.Client(account, token)

  user_number = context.json["phoneNumber"]
  msg = "Hello {} your authentication code is: {}.".format(user, code)
  message = client.api.account.messages.create(to=user_number,
                                               from_="+12065251212",
                                               body=msg)
  return {"status": "ok"}
