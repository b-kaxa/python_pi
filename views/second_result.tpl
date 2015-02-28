<!DOCTYPE html>
<html>
  <head>
    <meta charset = "UTF-8" />
    <title>pi</title>
  </head>
  <body>
    <p>{{search_result}}</p>
    <p>現在の得点は{{score_result}}です</p>
    <form action = "/final_result/" method="POST">
      <input type="number" name="third_number">
      <input type="submit" value="送信">
      <input type="hidden" name="total_score" value="{{score_result}}">
    </form>
  </body>
</html>
