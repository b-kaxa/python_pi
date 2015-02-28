<!DOCTYPE html>
<html>
  <head>
    <title>pi</title>
    <meta charset = "UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script type="text/javascript" src="{{ get_url('static', path='jquery/dist/jquery.min.js') }}" charset="utf-8"></script>
    <link rel="stylesheet" href="{{ get_url('static', path='bootstrap/dist/css/bootstrap.min.css') }}">
    <link rel="stylesheet" href="{{ get_url('original', path='original_style.css') }}">
  </head>
  <body>
      <nav class="navbar navbar-default navbar-fixed-top">
        <div class="container">
          <p class="navbar-text">円周率10000桁にあなたが選んだ数字はあるかな？</p>
        </div>
      </nav>
      <div class="container">
        <div class="panel panel-success">
          <div class="panel-heading">
            <h3 class="panel-title">遊び方</h3>
          </div>
          <div class="panel-body">
            <p>１・好きな数字を入力してください。</p>
            <p>２・その数字が円周率10000桁のどこにあるか表示します</p>
            <p>３・その数字の最終位が得点です</p>
            <p>４・合計三回の総得点が最後に出ます</p>
          </div>
        </div>
      <form action="/first_result/" method="POST">
        <input type="number" name="first_number">
        <input type="submit" value="送信">
      </form>
    </div>
  </body>
</html>