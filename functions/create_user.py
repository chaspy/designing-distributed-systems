def create_user(context):
  # 必須のイベントハンドラは全て呼び出す
  for key, value in required.items():
    call_function(value.webhook, context.json)

  # 任意のイベントハンドラは条件をチェックし合致するなら呼び出す
  for key, value in optional.items():
    if context.json.get(key, None) is not None:
      call_function(value.webhook, context.json)
