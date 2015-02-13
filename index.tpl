<!DOCTYPE html>
<html>
  <head>
    <meta charset = "UTF-8" />
    <title>pi</title>
  </head>
  <body>
    <h3>円周率10000桁にあなたが選んだ数字はあるかな？</h3>
    <h4>１・好きな数字を入力してください。</h4>
    <h4>２・その数字が円周率10000桁のどこにあるか表示します</h4>
    <h4>３・その数字の最終位が得点です</h4>
    <h4>４・合計三回の総得点が最後に出ます</h4>
    <form action="/first_result/" method="POST">
      <input type="number" name="first_number">
      <input type="submit" value="送信">
    </form>
  </body>
</html>