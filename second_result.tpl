<!DOCTYPE html>
<html>
  <head>
    <meta charset = "UTF-8" />
    <title>電力使用状況グラフ</title>
  </head>
  <body>
    <p>{{search_result}}</p>
    <form action = "/second_result/" method="POST">
      <input type="number" name="second_number">
      <input type="submit" value="送信">
    </form>
  </body>
</html>
