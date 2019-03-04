# デフォルト値で埋めるシンプルなハンドラ関数
def handler(context):
  # 入力値を取得
  obj = context.json
  # nameフィールドがなかったら、ランダムな値をセット
  if obj.get("name", None) is None:
    obj["name"] = random_name()
  # colorフィールドがなかったら、blueをセット
  if obj.get("color", None) is None:
    obj["color"] = "blue"
  # 新しいデフォルト値込みで、実際のAPIを呼び出し、
  # 結果をreturn
  return call_my_api(obj)
